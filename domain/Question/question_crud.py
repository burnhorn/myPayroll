from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Question
from domain.Question import question_schema

# Question 모델 객체 반환하여 DB에 반영
def create_question(db:Session, question_create:question_schema.QuestionCreate) -> Question:
    question = Question(**question_create.dict())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question



# id에 맞는 질문글(Model 객체) 찾는 함수
def get_question(db:Session, question_id:int) -> Question | None:
    result = db.execute(select(Question).filter(Question.id == question_id))
    return result.scalars().first()
    

# get_question 함수로 얻은 객체를 사용하여 DB에 있는 데이터에 새로운 입력값을 반영하는 함수
def update_question(db:Session, question_update:question_schema.QuestionCreate, question_original : Question) -> Question:
    question_original.title = question_update.title
    question_original.content = question_update.content
    db.add(question_original)
    db.commit()
    db.refresh(question_original)
    return question_original