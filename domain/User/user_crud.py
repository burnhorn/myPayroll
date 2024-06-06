from sqlalchemy.orm import Session
from domain.User import user_schema
from models import User

# User 모델 객체에 uer_create 스키마 제한값 할당 
def create_user(db:Session, user_create :user_schema.UserCreate) -> User:
    #user = User(**user_create.dict())
    user = User(user_name = user_create.user_name, password = user_create.password1, email = user_create.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
