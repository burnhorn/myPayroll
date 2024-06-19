import datetime
from pydantic import BaseModel, Field

from domain.User.user_schema import UserInfo


class AnswerBase(BaseModel):
    content : str | None = Field(None, example = "답변이 제대로 됐나요?")
    create_date : datetime.datetime
    
    
class AnswerCreate(BaseModel):
    content : str | None = Field(None, example = "답변이 제대로 됐나요?")

class AnswerUpdate(AnswerBase):
    pass

class AnswerDelete(AnswerBase):
    id : int

class AnswerCreateResponse(AnswerBase):
    id : int
    answer_user : UserInfo | None  # User 객체의 스키마를 가져와 Answer 라우터의 응답값에 추가 (User 모델과 relationship된 항목)