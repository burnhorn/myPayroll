from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from domain.User import user_schema
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User 모델 객체에 uer_create 스키마 제한값 할당 
def create_user(db:Session, user_create :user_schema.UserCreate) -> User:
    #user = User(**user_create.dict())
    user = User(user_name = user_create.user_name, password = user_create.password1, email = user_create.email)
    user = User(user_name = user_create.user_name,
                password = pwd_context(user_create.password1),
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
    


def fake_decode_token(db:Session, token) -> User:
    user = get_user(db, token)
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user