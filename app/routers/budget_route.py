# routers/budget_route.py
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.expense_model import Expense
from app.models.budget_model import Budget  #importing the table
from app.schema.budget_schema import BudgetCreate
from app.schema.budget_schema import BudgetResponse
from app.schema.budget_schema import BudgetUpdate
from app.database import  SessionLocal
from config import get_db
router = APIRouter()

@router.post("/budget") #creates and sets a budget
async def create_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    db_budget = Budget(
        month = budget.month,
        year = budget.year,
        amount = budget.amount,
    )

    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget


@router.get("/budget/status/")
def get_budget_status(month: str, year: int, db: Session = Depends(get_db)):
    # Fetch the budget for the given month and year
    budget = db.query(Budget).filter(month == Budget.month, year == Budget.year).first()

    if not budget:
        raise HTTPException(status_code=404, detail="Budget not set for this month and year.")

    # Fetch total expenses for that month and year
    expenses = db.query(Expense).all()  # You can optimize this later
    total_spent = sum(
        e.amount for e in expenses if e.date.month == datetime.strptime(month, "%B").month and e.date.year == year
    )

    percent_spent = (total_spent / budget.amount) * 100 if budget.amount else 0

    # Generate warning
    warning = None
    if percent_spent > 90:
        warning = "You've crossed 90% of your budget!"
    elif percent_spent > 70:
        warning = "You're above 70% of your budget."
    elif percent_spent > 50:
        warning = "You've spent over half your budget."

    return {
        "month": month,
        "year": year,
        "budget_limit": budget.amount,
        "total_spent": total_spent,
        "percent_spent": round(percent_spent, 2),
        "warning": warning or "All good. You're within budget."
    }

@router.get("/budgets/")
def get_budgets(db: Session = Depends(get_db)):
    return db.query(Budget).order_by(Budget.year, Budget.month).all()

@router.put("/budgets/")
def update_budget(budget_update: BudgetUpdate, db: Session = Depends(get_db)):
    existing_budget = db.query(Budget).filter(
        budget_update.month == Budget.month,
        budget_update.year == Budget.year
    ).first()

    if not existing_budget:
        raise HTTPException(status_code=404, detail="Budget not found.")

    existing_budget.amount = budget_update.amount
    db.commit()
    db.refresh(existing_budget)
    return existing_budget
