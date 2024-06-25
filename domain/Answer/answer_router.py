from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import Body
from domain.Answer import answer_schema, answer_crud
from domain.User import user_router

from database import get_db
from models import User

router = APIRouter(
    prefix = "/api/answer"
)


@router.get("/get/{answer_id}", response_model = answer_schema.AnswerCreateResponse)
async def get_answer(answer_id : int, db:Session = Depends(get_db)):
    return answer_crud.get_answer(db, answer_id)

@router.post("/create/{question_id}", response_model= answer_schema.AnswerCreateResponse)
async def create_answer(
    question_id : int,
    answer_body : answer_schema.AnswerCreate,  # [주의!] FastAPI 자동 인식으로 ':' 사용 시 request body, '=' 사용시 query 로 인식
    db:Session = Depends(get_db),
    current_user: User = Depends(user_router.get_current_user)):
    
    question = answer_crud.get_questionForAnswer(db, question_id = question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question Not Found")
    
    if current_user.id != question.answers.user_id:
        raise HTTPException(status_code = 404, detail = "Unauthorized users")
    
    return answer_crud.create_answer(db, answer_create = answer_body, question = question, user = current_user)

# 질문 객체를 가져와 request body 입력값을 db에 전달하여 질문 수정 함수    
@router.put("/update/{answer_id}", response_model=answer_schema.AnswerCreateResponse)
async def update_answer(
    answer_id : int,
    answer_body : answer_schema.AnswerUpdate,
    db : Session = Depends(get_db),
    current_user: User = Depends(user_router.get_current_user)):

    answer = answer_crud.get_answer(db, answer_id)

    if not answer:
        raise HTTPException(status_code=404, detail = "Answer Not Found")
    if current_user.id != answer.user_id:
        raise HTTPException(status_code = 404, detail = "Unauthorized users")
    return answer_crud.update_answer(db, answer_body, answer_original = answer )

@router.delete("/delete/{answer_id}")
async def delete_question(answer_id : int, db:Session = Depends(get_db), current_user: User = Depends(user_router.get_current_user)):
    answer = answer_crud.get_answer(db, answer_id = answer_id)
    if answer is None:
        raise HTTPException(status_code= 404, detail = "Data Not Found")
    if current_user.id != answer.user_id:
        raise HTTPException(status_code = 404, detail = "Unauthorized users")

    return answer_crud.delete_answer(db, answer_select=answer) 
