from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Used when creating a new expense
class ExpenseCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    category: str
    description: Optional[str] = None
    date: Optional[datetime] = None
    # No need to include `username` here since you'll get it from token in backend

# Used when returning an expense (e.g., GET or POST response)
class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: Optional[str]
    date: datetime
    username: str  # <-- Add this

    class Config:
        orm_mode = True  # Enables ORM to Pydantic conversion

# Used when updating an expense
class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0, description="Amount must be greater than zero")
    category: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
