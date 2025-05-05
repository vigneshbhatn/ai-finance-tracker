from pydantic import BaseModel, Field
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Used when creating a new expense
class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    category: str
    description: Optional[str] = None
    date: Optional[datetime] = None

# Used when returning an expense (e.g., GET or POST response)
class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: Optional[str]
    date: datetime

    class Config:
        orm_mode = True  # This tells Pydantic to read data from SQLAlchemy objects


class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(..., gt=0, description="Amount must be greater than zero")
    category: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None