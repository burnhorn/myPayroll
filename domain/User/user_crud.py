from datetime import datetime, timedelta, timezone

from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from domain.User import user_schema, user_schema
from models import User

from passlib.context import CryptContext
import jwt

from starlette.config import Config

# 환경 변수로 처리
config = Config('.env')
ACCESS_TOKEN_EXPIRE_MINUTES = int(config('ACCESS_TOKEN_EXPIRE_MINUTES'))
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = "HS256"

# 암호화
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

# User 모델 객체에 uer_create 스키마 제한값 할당 
def create_user(db:Session, user_create :user_schema.UserCreate) -> User:
    #user = User(**user_create.dict())
    user = User(user_name = user_create.user_name, password = user_create.password1, email = user_create.email)
    user = User(user_name = user_create.user_name,
                password = get_password_hash(user_create.password1),
                email = user_create.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# User 모델의 name과 email의 unique 적용 확인 함수
def check_user(db:Session, user_create :user_schema.UserCreate):
    result = db.execute(
        select(User).filter(
            or_(
                User.user_name == user_create.user_name,
                User.email == user_create.email
                )
            )
    )
    return result.scalars().first()

def get_user(db:Session, user_name : str) -> User:
    result = db.execute(
        select(User).filter(
                User.user_name == user_name
            )
    )
    return result.scalars().first()
    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str) -> User:
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


# token 엔드포인트에 사용될 Pydantic 모델 스키마
# 딕셔너리 타입의 입력값을 받는다
# exipires 입력값에 따라 만료시간 설정(기본 30분)
# to_encode 딕셔너리에 exp 키 추가
# JWT 인코딩하여 JWT 객체 생성 (만료시간 설정 토큰)
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    KST = timezone(timedelta(hours=9))
    if expires_delta:
        expire = datetime.now(KST) + expires_delta
    else:
        expire = datetime.now(KST) + timedelta(minutes = 15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
