# models/expense_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base= declarative_base()

class Earning(Base):
    __tablename__ = 'earnings'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each expense.
    amount = Column(Float, nullable=False)
    source = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False)