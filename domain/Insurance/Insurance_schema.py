# FastAPI의 스키마 모델
from pydantic import BaseModel, Field

class SalaryBase(BaseModel):
    salary : int 

class SalaryCreate(SalaryBase):
    pass

class SalaryCreateResponse(SalaryCreate):
    id: int


class InsuranceRateBase(BaseModel):
    national_pension : float
    health_insurance : float
    medical_insurance : float
    industrial_accident_insurance : float
    employment_insurance : float
    
    
class InsuranceRateCal(InsuranceRateBase):
    pass 

class NewPoeple(BaseModel):
    id : int