# create_tables.py
from app.database import engine
from app.models import Base  # Unified Base
from app.models import user_model, budget_model, earning_model, expense_model  # Import to register models

Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
