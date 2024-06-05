from pydantic import BaseModel, Field

class AnswerBase(BaseModel):
    content : str | None = Field(None, example = "답변이 제대로 됐나요?")

class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
    id : int

class AnswerDelete(AnswerBase):
    id : int

class AnswerCreateResponse(AnswerCreate):
    pass