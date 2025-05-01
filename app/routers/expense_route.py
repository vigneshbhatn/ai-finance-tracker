# routers/expense.py
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.expense_model import Expense  #importing the table
from app.schema.expense_schema import ExpenseCreate
from app.schema.expense_schema import ExpenseUpdate
from app.database import  SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # This gets the database session.
    try:
        yield db # this one connects to the db
    finally:
        db.close()

@router.post("/expense/")  # creates the expense
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

@router.get("/expenses/")  #Reads all the expenses
def read_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()


@router.delete("/expense/{expense_id}") #deletes the expense
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(expense_id == Expense.id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()
    return {"message": "Expense deleted"}

@router.put("/expense/{expense_id}") #updates the given expenses accorindit to the id
def update_expense(expense_id: int, updated_data: ExpenseUpdate, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(expense_id == Expense.id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    # Update only the fields that are provided
    if updated_data.amount is not None:
        expense.amount = updated_data.amount
    if updated_data.category is not None:
        expense.category = updated_data.category
    if updated_data.description is not None:
        expense.description = updated_data.description
    if updated_data.date is not None:
        expense.date = updated_data.date

    db.commit()
    db.refresh(expense)
    return expense