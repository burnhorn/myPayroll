from pydantic import BaseModel, Field
import datetime

from domain.Answer.answer_schema import AnswerCreateResponse
from domain.User.user_schema import UserInfo

class QuestionBase(BaseModel):
    id : int
    title : str | None = Field(None, example = "작성이 제대로 됐나요?")
    content : str | None = Field(None, example = "더미데이터")
    create_date : datetime.datetime
    
class QuestionCreate(BaseModel):
    title : str | None = Field(None, example = "작성이 제대로 됐나요?")
    content : str | None = Field(None, example = "더미데이터")
    
class QuestionUpdate(QuestionBase):
    pass

class QuestionDelete(QuestionBase):
    id : int    

# response_model로 사용하여 작성된 질문 데이터가 어디에 있는지 확인하는 용도
class QuestionCreateResponse(QuestionBase):
    question_user : UserInfo | None  # User 객체의 스키마를 가져와 Question 라우터의 응답값에 추가 (User 모델과 relationship된 항목)
    answers : list[AnswerCreateResponse]  # 여러 Answer 객체를 가져와야 하므로 []로 처리

class QuestionList(BaseModel):
    id : int
    title : str
    create_date : datetime.datetime
    user_name : str | None  # in case that user_name is not in DB, None type is effective.

class QuestionListPage(BaseModel):
    question_list: list[QuestionList]
    question_total: int