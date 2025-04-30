from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Used when creating a new expense
class ExpenseCreate(BaseModel):
    amount: float
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
