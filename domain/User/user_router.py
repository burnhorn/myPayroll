from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import User

from domain.User import user_schema, user_crud
from database import get_db

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import jwt
from jwt.exceptions import InvalidTokenError

router = APIRouter(
    prefix = "/api/user"
)

# Authorize 버튼의 username과 password 값을 받을 경로
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/token")

@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
async def create_user(user_body : user_schema.UserCreate, db: Session = Depends(get_db)):
    if user_crud.check_user(db, user_create = user_body):
        raise (HTTPException(status_code=status.HTTP_409_CONFLICT, detail = "동일한 사용자가 존재합니다."))
    return user_crud.create_user(db, user_body)

# OAuth2PasswordRequestForm : Authorize버튼의 username과 passowrd 값을 가져올 수 있다.(매핑)
@router.post("/token") # form_data는 문자열이므로 스키마로 받을 수 없음
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> user_schema.Token :
    # 정상 유저 확인
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers = {"WWW-Authenticate" : "Bearer"},
            )
    # aceess_token 확인
    access_token_expires = timedelta(minutes = user_crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token에 sub(정상 유저의 user_name)과 exp 키 추가
    access_token = user_crud.create_access_token(
        data = {"sub":user.user_name},
                expires_delta = access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# token 값은 oauth2_scheme->@router.post("/token")에서 얻어진 "access_token"
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate" : "Bearer"},
    )
    # jwt 인코딩을 디코딩하여 sub키에 접근하여 정상 유저의 user_name을 가져온다
    # TokenData 스키마를 활용하여 입출력값을 제한하여 오류 방지
    try:
        payload = jwt.decode(token, user_crud.SECRET_KEY, algorithms = [user_crud.ALGORITHM])
        user_name : str = payload.get("sub")
        if user_name is None:
            raise credentials_exception
        token_data = user_schema.TokenData(username = user_name)
    except InvalidTokenError:
        raise credentials_exception
    # get_user 매개변수(정의), 인자(전달값) 오류가 안 나도록 주의
    user = user_crud.get_user(db, user_name = token_data.username)
    if user is None:
        raise credentials_exception
    return user

# 인증 기능 구현 및 현재 유저 값 확인
@router.get("/me")
async def read_user(current_user: Annotated[str, Depends(get_current_user)]):
    return current_user