# routers/expense.py
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.expense_model import Expense
from app.schema.expense_schema import ExpenseCreate
from app.database import  SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # This gets the database session.
    try:
        yield db
    finally:
        db.close()

@router.post("/expense/")
async def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    # Create a new expense object using the data received in the request.
    db_expense = Expense(
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        date=expense.date or datetime.utcnow()  # If no date is provided, use the current date.
    )
    
    db.add(db_expense)  # Add the expense to the database.
    db.commit()  # Commit the transaction (save it in the database).
    db.refresh(db_expense)  # Refresh the expense object to get the updated data (e.g., ID).
    
    return db_expense  # Return the created expense (as a response).
