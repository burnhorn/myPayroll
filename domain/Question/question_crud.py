from datetime import datetime
from typing import Tuple

from sqlalchemy import DateTime, Result, func, select
from sqlalchemy.orm import Session

from models import Question, User
from domain.Question import question_schema

# Question 모델 객체 반환하여 DB에 반영
def create_question(db:Session, question_create:question_schema.QuestionCreate, user : User) -> Question:
    question = Question(title=question_create.title,
                        content=question_create.content,
                        create_date=datetime.now(),
                        question_user = user)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

# id에 맞는 질문글(Model 객체) 찾는 함수
def get_question(db:Session, question_id:int) -> Question | None:
    result = db.execute(select(Question).filter(Question.id == question_id))
    return result.scalars().first()

# Quesiton 테이블과 User 테이블 조인하여 User.user_name 가져오기
def get_question_list(db: Session, skip: int = 0, limit: int = 20) -> Tuple[int, list[dict]]:
    question_total = db.execute(select(func.count(Question.id))).scalar_one()

    query = select(
        Question.id,
        Question.title,
        Question.content,
        Question.create_date,
        User.user_name.label('user_name')
    ).outerjoin(User, Question.user_id == User.id).offset(skip).limit(limit)

    result = db.execute(query)
    
    question_list = []
    for row in result:
        question = {
            "id": row.id,
            "title": row.title,
            "content": row.content,
            "create_date": row.create_date,
            "user_name": row.user_name
        }
        question_list.append(question)
    
    return question_total, question_list


# get_question 함수로 얻은 객체를 사용하여 DB에 있는 데이터에 새로운 입력값을 반영하는 함수
def update_question(db:Session, question_update:question_schema.QuestionCreate, question_original : Question) -> Question:
    question_original.title = question_update.title
    question_original.content = question_update.content
    db.add(question_original)
    db.commit()
    db.refresh(question_original)
    return question_original

# get_question 함수로 얻는 객체(model)를 사용하여 db에 데이터를 삭제하는 함수
def delete_question(db:Session, question_select : Question) -> None:
    db.delete(question_select)
    db.commit()
