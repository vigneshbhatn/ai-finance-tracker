# create_tables.py
from app.util.database import engine
from app.models import Base

# ✅ Import all model classes so they're registered with Base
from app.models.user_model import User
from app.models.expense_model import Expense
from app.models.budget_model import Budget
from app.models.earning_model import Earning

Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
