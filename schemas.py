from typing import List  
from pydantic import BaseModel

# User

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

# Category

class CategoryBase(BaseModel):
    name: str
    description: str
    is_active: bool
    id_user: int

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class PaginatedCategory(BaseModel):
    limit: int
    offset: int
    data: List[Category]


# Account
class AccountBase(BaseModel):
    name: str
    is_active: bool

class Account(AccountBase):
    id: int
    class Config:
        orm_mode = True
