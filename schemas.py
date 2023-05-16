from datetime import date
from typing import List  
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
class UserCreate(UserBase):
    password: str
class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserLoginSchema(BaseModel):
    email: str
    password: str
    class Config:
        schema_extra = {
            "example": {
                "email": "x@x.com",
                "password": "pass"
            }
        }

class PaginatedUser(BaseModel):
    limit: int
    offset: int
    data: List[User]