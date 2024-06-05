from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import Body
from domain.Answer import answer_schema, answer_crud
from database import get_db

router = APIRouter(
    prefix = "/api/answer"
)


@router.get("/get/{question_id}", response_model = answer_schema.AnswerBase)
async def get_question():
    pass

@router.post("/create/{question_id}", response_model= answer_schema.AnswerCreateResponse)
async def create_answer(
    question_id : int,
    answer_body : answer_schema.AnswerCreate,  # [주의!] FastAPI 자동 인식으로 ':' 사용 시 request body, '=' 사용시 query 로 인식
    db:Session = Depends(get_db)):
    
    question = answer_crud.get_questionForAnswer(db, question_id = question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question Not Found")
    return answer_crud.create_answer(db, answer_body, question)
    
@router.put("/update/{answer_id}")
async def update_question():
    pass

@router.delete("delete/{answer_id}")
async def delete_question():
    pass
