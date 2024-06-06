from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from domain.User import user_schema, user_crud
from database import get_db

router = APIRouter(
    prefix = "/api/user"
)


@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
async def create_user(user_body : user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user_body)