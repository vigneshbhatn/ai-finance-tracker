# models/budget_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import UniqueConstraint
Base = declarative_base()

class Budget(Base):
    __tablename__ = 'budgets'
    __table_args__ = (UniqueConstraint('month', 'year', name='unique_month_year'),) #adding this so that the years and months are unique
    id = Column(Integer, primary_key=True, index=True)
    month = Column(String(20), nullable=False)
    year = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
