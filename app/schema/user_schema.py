from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str  # Plain password sent by user

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
