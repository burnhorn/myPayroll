from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base

class InsuranceRate(Base):
    __tablename__ = "4_Major_Insurance_rates"

    id = Column(Integer, primary_key=True, index=True)
    national_pension = Column(Float, nullable=False)
    health_insurance = Column(Float, nullable=False)
    medical_insurance = Column(Float, nullable=False)
    industrial_accident_insurance = Column(Float, nullable=False)
    employment_insurance = Column(Float, nullable=False)

    # newpeople = relationship("NewPeople", back_populates="rates")
    

"""
class NewPoeple(Base):
    __tablename__ = "Not_Insurance_People"

    id = Column(Integer, ForeignKey('4_Major_Insurance_rates.id'), primary_key=True)
    name = Column(String(1024), nullable=False)
    emp_num = Column(String(1024), nullable=False) 

    rate = relationship("InsureanceRate", back_populates="newpoeple")
"""

class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key = True, index= True)
    title = Column(String(1024))
    content = Column(Text, nullable= False)
    answers = relationship("Answer", back_populates="question", cascade = "delete")
    create_date = Column(DateTime, nullable = False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key = True, index = True)
    content = Column(Text, nullable= False)
    question_id = Column(Integer, ForeignKey('question.id'))       # ForeignKey와 relationship 기능을 통해 Question과 Answer 모델 연결하여 질문에 달린 답변, 답변이 있는 질문 접근
    question = relationship("Question", back_populates="answers")  # answers.question으로 접근
    create_date = Column(DateTime, nullable = False)
