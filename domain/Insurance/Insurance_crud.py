from sqlalchemy.orm import Session
from sqlalchemy import select
from models import InsuranceRate

import math

def get_rate(db: Session):
    return db.execute(select(InsuranceRate)).scalars().first()


# 원단위 절사 (국민연금 기준소득월액 1000원 미만 절사 추가 예정)
def get_value(db: Session, salary):
    rate = db.execute(select(InsuranceRate)).scalars().first()
    if salary <= 390000:
        calculated_values = {
        "national_pension": math.floor(390000 * rate.national_pension / 10) * 10,
        "health_insurance": math.floor(salary * rate.health_insurance / 10) * 10,
        "medical_insurance": None,
        "industrial_accident_insurance": math.floor(salary * rate.industrial_accident_insurance / 10) * 10,
        "employment_insurance": math.floor(salary * rate.employment_insurance / 10) * 10
    }     
    elif 390000 < salary < 6170000:
        calculated_values = {
        "national_pension": math.floor(salary * rate.national_pension / 10) * 10,
        "health_insurance": math.floor(salary * rate.health_insurance / 10) * 10,
        "medical_insurance": None,
        "industrial_accident_insurance": math.floor(salary * rate.industrial_accident_insurance / 10) * 10,
        "employment_insurance": math.floor(salary * rate.employment_insurance / 10) * 10
    }    
    else:
        calculated_values = {
        "national_pension": math.floor(6170000 * rate.national_pension / 10) * 10,
        "health_insurance": math.floor(salary * rate.health_insurance / 10) * 10,
        "medical_insurance": None,
        "industrial_accident_insurance": math.floor(salary * rate.industrial_accident_insurance / 10) * 10,
        "employment_insurance": math.floor(salary * rate.employment_insurance / 10) * 10
    }
    calculated_values["medical_insurance"] = math.floor(calculated_values["health_insurance"] * rate.medical_insurance / 10) * 10
    return calculated_values


# 키:값 형태로 4대보험 요율 데이터 전달
def update_rate(db: Session, rate_id: int, new_values: dict):
    rate = db.query(InsuranceRate).filter(InsuranceRate.id == rate_id).first()
    if not rate:
        return None
    for key, value in new_values.items():
        setattr(rate, key, value)
    db.commit()
    db.refresh(rate)
    return rate