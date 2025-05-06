from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserModel(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str

class UserCreate(UserModel):
    pass

class UserResponse(UserModel):
    id: int

    class Config:
        orn_mode = True