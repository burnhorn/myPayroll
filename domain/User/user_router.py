from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from domain.User import user_schema, user_crud
from database import get_db

from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models import User


router = APIRouter(
    prefix = "/api/user"
)

# Authorize 버튼의 username과 password 값을 받을 경로
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/token")

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
async def create_user(user_body : user_schema.UserCreate, db: Session = Depends(get_db)):
    if user_crud.check_user(db, user_create = user_body):
        raise (HTTPException(status_code=status.HTTP_409_CONFLICT, detail = "동일한 사용자가 존재합니다."))
    return user_crud.create_user(db, user_body)

# OAuth2PasswordRequestForm : Authorize버튼의 username과 passowrd 값을 가져올 수 있다.
@router.post("/token") # form_data는 문자열이므로 스키마로 받을 수 없음
async def tokenForLogin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # 토큰 생성 알고리즘이 없으므로 반환받은 User 객체의 user_name 항목을 출력
    return {"access_token": user.user_name, "token_type": "bearer"}

# token 값은 oauth2_scheme->@router.post("/token")에서 얻어진 "access_token"
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
    user = user_crud.fake_decode_token(db, token)
    if not user:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return user


@router.get("/me")
async def read_user(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user