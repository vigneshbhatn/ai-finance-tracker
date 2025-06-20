from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://vignesh:vignesh123@localhost/finance_tracker"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency function for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from sqlalchemy.orm import Session
from app.models.user_model import User# adjust import based on your folder structure

def get_user_by_username(db: Session , username: str):
    return db.query(User).filter(username == User.username).first()
