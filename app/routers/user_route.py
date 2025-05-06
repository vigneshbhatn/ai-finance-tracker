from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schema.user_schema  import UserCreate
from app.schema.user_schema  import UserResponse
from config import get_db

router = APIRouter()

@router.post("/signup")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(

    )