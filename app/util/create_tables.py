# create_tables.py
from app.util.database import engine
from app.models import Base  # Unified Base

Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
