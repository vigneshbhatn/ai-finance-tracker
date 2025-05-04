# models/expense_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'  # This defines the name of the table in the database.
    
    # Define columns (fields) in the expenses table.
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each expense.
    amount = Column(Float, nullable=False)  # Amount spent (must be a number).
    category = Column(String(100), nullable=False)  # Category of the expense (e.g., Food, Transportation).
    description = Column(String(255), nullable=True)  # Optional description.
    date = Column(DateTime, default=datetime, nullable=False)  # Date of expense (defaults to current time).
