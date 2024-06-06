from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing_extensions import Self

class UserBase(BaseModel):
    user_name: str
    password1: str
    password2: str
    email: EmailStr

    @field_validator('user_name', 'password1', 'password2', 'email')
    @classmethod
    def name_must_contain_value(cls, values: str) -> str:
        if not values or ' ' in values :
            raise ValueError('must contain values')
        return values

class UserCreate(UserBase):
    pass

class UserCreateResponse(UserCreate):
    pass