from pydantic import BaseModel, Field
import datetime

class QuestionBase(BaseModel):
    id : int
    title : str | None = Field(None, example = "작성이 제대로 됐나요?")
    content : str | None = Field(None, example = "더미데이터")

class QuestionCreate(BaseModel):
    title : str | None = Field(None, example = "작성이 제대로 됐나요?")
    content : str | None = Field(None, example = "더미데이터")
    create_date : datetime.datetime
    
class QuestionUpdate(QuestionBase):
    pass

class QuestionDelete(QuestionBase):
    id : int    

# response_model로 사용하여 작성된 질문 데이터가 어디에 있는지 확인하는 용도
class QuestionCreateResponse(QuestionCreate):
    pass

class QuestionList(BaseModel):
    id : int
    title : str
    create_date : datetime.datetime
    user_name: str