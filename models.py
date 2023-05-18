from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base
import enum

class Types(enum.Enum):
    income = "INCOME"
    expense = "EXPENSE"

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    email = Column(String(150), unique=True, index=True)
    password = Column(String(255))
    categories = relationship("Category", back_populates="user")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    description = Column(String(500))
    type = Column('type', Enum(Types))
    is_active = Column(Boolean, default=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="categories")