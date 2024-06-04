from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import domain.Insurance.Insurance_schema as salary_schema
import domain.Insurance.Insurance_crud as salary_crud



router = APIRouter(
    prefix = "/api/insurance"
)

# response_model 설정을 통해 라우터의 반환값이 반환 타입(스키마)과 일치해야 한다.
@router.get("/rates", response_model=salary_schema.InsuranceRateBase)
async def insurance(db: Session = Depends(get_db)):
    rates = salary_crud.get_rate(db)
    return rates

# 급여에 따른 4대보험료
@router.get("/calculate", response_model=salary_schema.InsuranceRateBase)
async def calculate_insurance(db: Session = Depends(get_db), salary : int = Query(..., description="Input Your Salary")):
    
    value = salary_crud.get_value(db, salary)

    return value
    

# 4대보험요율 변경
@router.put("/update/{rate_id}", response_model=salary_schema.InsuranceRateBase)
async def update_insurance_rate(rate_id: int, new_values: dict, db: Session = Depends(get_db)):
    updated_rate = salary_crud.update_rate(db, rate_id, new_values)
    if updated_rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    return updated_rate