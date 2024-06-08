from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing_extensions import Self

class UserBase(BaseModel):
    user_name: str
    
class UserCreate(UserBase):
    email: EmailStr
    password1: str
    password2: str

    @field_validator('user_name', 'password1', 'password2', 'email')
    @classmethod
    def name_must_contain_value(cls, values: str) -> str:
        if not values or ' ' in values :
            raise ValueError('입력을 확인해 주세요')
        return values
    
    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        pw1 = self.password1
        pw2 = self.password2
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('비밀번호가 다릅니다')
        return self

class UserInDB(UserBase):
    passwword : str


class UserCreateResponse(UserCreate):
    pass