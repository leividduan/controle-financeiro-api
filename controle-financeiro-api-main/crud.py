from sqlalchemy.orm import Session
from exceptions import *
import bcrypt, models, schemas

# User
def check_user(db: Session, user: schemas.UserLoginSchema):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user is None:
        return False
    return bcrypt.checkpw(user.password.encode('utf8'), db_user.password.encode('utf8'))

def get_user_by_id(db: Session, user_id: int):
    db_user = db.query(models.User).get(user_id)
    if db_user is None:
        raise UserNotFoundError
    return db_user

def get_all_users(db: Session, offset: int, limit: int):
    return db.query(models.User).offset(offset).limit(limit).all()

def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = get_user_by_email(db, user.email)
    # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
    user.password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
    if db_user is not None:
        raise UserAlreadyExistError
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = get_user_by_id(db, user_id)
    db_user.name = user.name
    db_user.email = user.email
    if user.password != "":
        # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
        db_user.password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt())
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_by_id(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    db.delete(db_user)
    db.commit()
    return

# Category
def get_all_categories(db: Session, offset: int, limit: int):
    return db.query(models.Category).offset(offset).limit(limit).all()

def get_category_by_id(db: Session, category_id: int):
    db_category = db.query(models.Category).get(category_id)
    if db_category is None:
        raise CategoryNotFoundError
    return db_category

def get_category_by_name(db: Session, category_name: str):
    return db.query(models.Category).filter(models.Category.name == category_name).first()

def create_category(db: Session, category: schemas.CategoryBase):
    db_category = get_category_by_name(db, category.name)
    if db_category is not None:
        raise CategoryAlreadyExistError
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, category: schemas.CategoryBase):
    db_category = get_category_by_id(db, category_id)
    db_category.name = category.name
    db_category.description = category.description
    db_category.is_active = category.is_active
    db_category.id_user = category.id_user
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category_by_id(db: Session, category_id: int):
    db_category = get_category_by_id(db, category_id)
    db.delete(db_category)
    db.commit()
    return

# Goals

def get_all_Goals(db: Session, offset: int, limit: int):
    return db.query(models.Goals).offset(offset).limit(limit).all()

def get_Goals_by_id(db: Session, Goals_id: int):
    db_Goals = db.query(models.Goals).get(Goals_id)
    if db_Goals is None:
        raise GoalsNotFoundError
    return db_Goals

def get_Goals_by_name(db: Session, Goals_name: str):
    return db.query(models.Goals).filter(models.Goals.name == Goals_name).first()

def create_Goals(db: Session, Goals: schemas.GoalsBase):
    db_Goals = get_Goals_by_name(db, Goals.name)
    if db_Goals is not None:
        raise GoalsAlreadyExistError
    db_Goals = models.Goals(**Goals.dict())
    db.add(db_Goals)
    db.commit()
    db.refresh(db_Goals)
    return db_Goals

def update_Goals(db: Session, Goals_id: int, Goals: schemas.GoalsBase):
    db_Goals = get_Goals_by_id(db, Goals_id)
    db_Goals.name = Goals.name
    db_Goals.description = Goals.description
    db_Goals.is_active = Goals.is_active
    db_Goals.id_user = Goals.id_user
    db.commit()
    db.refresh(db_Goals)
    return db_Goals
def delete_Goals_by_id(db: Session, Goals_id: int):
    db_Goals = get_Goals_by_id(db, Goals_id)
    db.delete(db_Goals)
    db.commit()
    return


# Report

# Accounts
def get_all_accounts(db: Session, offset: int, limit: int):
    return db.query(models.Account).offset(offset).limit(limit).all()

def get_account_by_id(db: Session, account_id: int):
    db_account = db.query(models.Account).get(account_id)
    if db_account is None:
        raise AccountNotFoundError
    return db_account

def get_account_by_name(db: Session, account_name:str):
    return db.query(models.Account).filter(models.Account.name == account_name).first()

def create_account(db: Session, account: schemas.AccountBase):
    db_account = get_account_by_name(db, account.name)
    if db_account is not None:
        raise AccountAlreadyExistError
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def update_account(db: Session, account_id: int, account: schemas.AccountBase):
    db_account = get_account_by_id(db, account_id)
    db_account.name = account.name
    db_account.is_active = account.is_active
    db_account.id_user = account.id_user
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account_by_id(db: Session, account_id: int):
    db_account = get_account_by_id(db, account_id)
    db.delete(db_account)
    db.commit()
    return

# Transaction
def get_all_transactions(db: Session, offset: int, limit: int):
    return db.query(models.Transaction).offset(offset).limit(limit).all()

def get_transaction_by_id(db: Session, transaction_id: int):
    db_transaction = db.query(models.Transaction).get(transaction_id)
    if db_transaction is None:
        raise TransactionNotFoundError
    return db_transaction

def get_transaction_by_name(db: Session, transaction_name:str):
    return db.query(models.Transaction).filter(models.Transaction.name == transaction_name).first()

def create_transaction(db: Session, transaction: schemas.TransactionBase):
    db_transaction = get_transaction_by_name(db, transaction.name)
    if db_transaction is not None:
        raise TransactionNotFoundError # rever
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def update_transaction(db: Session, transaction_id: int, transaction: schemas.TransactionBase):
    db_transaction = get_transaction_by_id(db, transaction_id)
    db_transaction.name = transaction.name
    db_transaction.is_active = transaction.is_active
    db_transaction.id_user = transaction.id_user
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def delete_transaction_by_id(db: Session, transaction_id: int):
    db_transaction = get_transaction_by_id(db, transaction_id)
    db.delete(db_transaction)
    db.commit()
    return