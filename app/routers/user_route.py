from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
router = APIRouter()

@router.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    return {"username": username}

from sqlalchemy.orm import Session
from app.util.config import get_db
from app.models.user_model import User
from app.schema.user_schema import UserCreate, UserResponse
from app.util.security import get_password_hash,verify_token  # this hashes passwords

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter(user.email == User.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = get_password_hash(user.password)

    # Create new user
    new_user = User(username= user.username, email=user.email, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    return {"username": username}