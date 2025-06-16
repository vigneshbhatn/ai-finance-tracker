# models/budget_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.models import Base
from datetime import datetime
from sqlalchemy import UniqueConstraint


class Budget(Base):
    __tablename__ = 'budgets'
    __table_args__ = (
        UniqueConstraint('user_id', 'month', 'year', name='unique_user_budget'),
    )

    id = Column(Integer, primary_key=True, index=True)
    month = Column(String(20), nullable=False)
    year = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
