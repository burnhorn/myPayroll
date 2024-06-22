from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from domain.Question import question_schema, question_crud
from domain.User import user_router
from database import get_db

from models import User

router = APIRouter(
    prefix = "/api/question"
)


# 질문 여러 개체를 CRUD에서 가져오므로 응답모델을 list로 설정
@router.get("/list", response_model = question_schema.QuestionListPage)
async def get_question_list(db:Session = Depends(get_db), page: int = 0, size: int = 20):
    question_total, question_list = question_crud.get_question_list(db, skip=page*size, limit=size)
    return {
        'question_total': question_total,
        'question_list' : question_list
    }

@router.get("/{question_id}", response_model = question_schema.QuestionCreateResponse)
async def get_question(question_id : int, db:Session = Depends(get_db)):
    return question_crud.get_question(db, question_id = question_id)


@router.post("/create", response_model = question_schema.QuestionCreateResponse)
async def create_question(question_body : question_schema.QuestionCreate,
                        db: Session = Depends(get_db),
                        current_user: User = Depends(user_router.get_current_user)): # get_current_user 함수는 Depends(oauth2_scheme)를 하고 있기에 인증 기능이 현 라우터에 추가된다. 또한 Depends 기능으로 현 라우터가 호출되자마자 User모델이 반환된다
    return question_crud.create_question(db, question_create = question_body, user = current_user)


@router.put("/update/{question_id}", response_model=question_schema.QuestionCreateResponse)
async def update_question(question_id : int,
                        question_body : question_schema.QuestionUpdate,
                        db:Session = Depends(get_db),
                        current_user: User = Depends(user_router.get_current_user)):
    question = question_crud.get_question(db, question_id = question_id)
    if question is None:
        raise HTTPException(status_code = 404, detail = "Data Not Found")
    if current_user.id != question.user_id:
        raise HTTPException(status_code = 404, detail = "Unauthorized users")

    return question_crud.update_question(db, question_body, question_original=question)

@router.delete("/delete/{question_id}", response_model = None)
async def delete_question(question_id : int,
                        db:Session = Depends(get_db),
                        current_user: User = Depends(user_router.get_current_user)):
    question = question_crud.get_question(db, question_id = question_id)
    if question is None:
        raise HTTPException(status_code = 404, detail = "Data Not Found")
    if current_user.id != question.user_id:
        raise HTTPException(status_code = 404, detail = "Unauthorized users")
    
    return question_crud.delete_question(db, question_select=question)  # question_select을 표기함으로써 매개변수의 역할에 대한 직관성을 확보
