from sqlalchemy import Column, Integer, String, Float, DateTime
from app.models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for each expense.
    username = Column(String(50),unique = True, index= True, nullable = False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)