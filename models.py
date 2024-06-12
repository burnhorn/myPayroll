from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base

# industrial_accident_insurance과 employment_insurance 순서 바꾸기
class InsuranceRate(Base):
    __tablename__ = "4_Major_Insurance_rates"

    id = Column(Integer, primary_key=True, index=True)
    national_pension = Column(Float, nullable=False)
    health_insurance = Column(Float, nullable=False)
    medical_insurance = Column(Float, nullable=False)
    industrial_accident_insurance = Column(Float, nullable=False)
    employment_insurance = Column(Float, nullable=False)

    # newpeople = relationship("NewPeople", back_populates="rates")
    
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(1024), unique=True, nullable=False)
    password = Column(String(1024), nullable=False) 
    email = Column(String(1024), unique=True, nullable=False)
    questions_user = relationship("Question", back_populates="question_user") # back_populates는 relationship으로 연결된 항목 이름과 일치해야 한다.
    answers_user = relationship("Answer", back_populates="answer_user")

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key = True, index= True)
    title = Column(String(1024))
    content = Column(Text, nullable= False)
    answers = relationship("Answer", back_populates="question", cascade = "delete")
    create_date = Column(DateTime, nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = True)
    question_user = relationship("User", back_populates="questions_user") # question_user 항목에 특정 User 모델을 저장하면 user_id 값에 자동으로 그 User 모델의 id가 저장된다

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key = True, index = True)
    content = Column(Text, nullable= False)
    question_id = Column(Integer, ForeignKey('question.id'))       # ForeignKey와 relationship 기능을 통해 Question과 Answer 모델 연결하여 질문에 달린 답변, 답변이 있는 질문 접근
    question = relationship("Question", back_populates="answers")  # answers.question으로 접근
    create_date = Column(DateTime, nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    answer_user = relationship("User", back_populates="answers_user")
