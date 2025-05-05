# create_tables.py
from app.database import engine
from app.models.expense_model import Base
from app.models.budget_model import Base
from app.models.earning_model import Base
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
