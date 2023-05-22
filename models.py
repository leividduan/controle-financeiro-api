from sqlalchemy import Column, Double, Integer, String, Enum, Date, ForeignKey, Table, Boolean
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
    goals = relationship("Goals", back_populates="user")
    accounts = relationship("Account", back_populates="user")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    description = Column(String(500))
    type = Column('type', Enum(Types))
    is_active = Column(Boolean, default=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="categories")
    goals = relationship("Goals", back_populates="category")
    transactions = relationship("Transaction", back_populates="category")

class Goals(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    is_active = Column(Boolean, default=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    id_category = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="goals")
    user = relationship("User", back_populates="goals")    

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    is_active = Column(Boolean, default=True)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150))
    description = Column(String(150))
    value = Column(Double)
    type = Column('type', Enum(Types))
    id_category = Column(Integer, ForeignKey("categories.id"), nullable=False)
    id_account = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    category = relationship("Category", back_populates="transactions")
    account = relationship("Account", back_populates="transactions")
