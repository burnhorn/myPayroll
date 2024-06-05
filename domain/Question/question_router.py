from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from domain.Question import question_schema, question_crud
from database import get_db

router = APIRouter(
    prefix = "/api"
)

# 질문 여러 개체를 CRUD에서 가져오므로 응답모델을 list로 설정
@router.get("/question/{quesiton_id}", response_model = question_schema.QuestionCreateResponse)
async def get_question(question_id : int, db:Session = Depends(get_db)):
    return question_crud.get_question(db, question_id = question_id)

@router.post("/question", response_model = question_schema.QuestionCreateResponse)
async def create_question(question_body : question_schema.QuestionCreate, db: Session = Depends(get_db)):
    return question_crud.create_question(db, question_body)


@router.put("/question/{question_id}", response_model=question_schema.QuestionCreateResponse)
async def update_question(question_id : int, question_body : question_schema.QuestionUpdate, db:Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id = question_id)
    if question is None:
        raise HTTPException(status_code = 404, detail = "Data Not Found")

    return question_crud.update_question(db, question_body, question_original=question)

@router.delete("/question/{question_id}", response_model = None)
async def delete_question(question_id : int, db:Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id = question_id)
    if question is None:
        raise HTTPException(status_code = 404, detail = "Data Not Found")
    
    return question_crud.delete_question(db, question_select=question)  # question_select을 표기함으로써 매개변수의 역할에 대한 직관성을 확보
