from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Answer, Question
from domain.Answer import answer_schema

from datetime import datetime

# 답변에 연결할 질문 객체 호출
def get_questionForAnswer(db:Session, question_id:int) -> Question | None:
    result = db.execute(select(Question).filter(Question.id == question_id))
    return result.scalars().first()

# 원하는 question_id와 content를 담은 답변 객체 전달
def create_answer(db:Session, answer_create : answer_schema.AnswerCreate, question : Question) -> Answer:
    # Answer 모델의 question 항목에 Question 객체를 전달하면 relationship과 ForeignKey 설정에 의해 question_id 자동 할당하므로 굳이 question_id를 라우터에서 가져올 필요 없다.
    db_answer = Answer(question = question, content = answer_create.content, create_date = datetime.now())  # model의 Integer 속성을 가진 항목 제외하고 모두 전달해야 insert 오류 안 나옴
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

# 질문 객체 찾는 함수
def get_answer(db:Session, answer_id:int) -> Answer | None:
    result = db.execute(select(Answer).filter(Answer.id == answer_id))
    return result.scalars().first()

# get_answer 함수로 얻은 Answer 객체를 사용하여 DB에 있는 데이터에 새로운 입력값 반영
def update_answer(db:Session, answer_update:answer_schema.AnswerUpdate, answer_original:Answer) -> Answer:
    answer_original.content = answer_update.content
    db.add(answer_original)
    db.commit()
    db.refresh(answer_original)
    return answer_original