from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional
from enum import Enum

class MonthEnum(str, Enum):
    January = "January"
    February = "February"
    March = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September = "September"
    October = "October"
    November = "November"
    December = "December"
# This is the schema for creating a new budget
class BudgetCreate(BaseModel):
    month: MonthEnum  # Month when the budget is set (e.g. 'April', 'May', etc.)
    year: int  # Year of the budget (e.g. 2025)
    amount: float  # The total amount of the budget for that month

    # This will automatically convert input to proper format
    class Config:
        orm_mode = True


# This is the schema for returning a budget after it's created or fetched
class BudgetResponse(BudgetCreate):
    id: int  # The ID that was assigned by the database
    created_at: datetime  # The timestamp when the budget was created

    class Config:
        orm_mode = True

class BudgetUpdate(BaseModel):
    month: MonthEnum
    year: int
    amount: float
