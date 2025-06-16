from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class EarningBase(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    source: str
    date: Optional[datetime] = None



class EarningCreate(EarningBase):
    pass

class EarningResponse(EarningBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True
