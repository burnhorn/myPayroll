from sqlalchemy import select, or_
from sqlalchemy.orm import Session
from domain.User import user_schema
from models import User
from passlib.context import CryptContext

myctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User 모델 객체에 uer_create 스키마 제한값 할당 
def create_user(db:Session, user_create :user_schema.UserCreate) -> User:
    #user = User(**user_create.dict())
    user = User(user_name = user_create.user_name,
                password = myctx.hash(user_create.password1),
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