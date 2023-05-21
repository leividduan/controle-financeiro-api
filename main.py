from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from exceptions import UserException, CategoryException, AccountException
from database import get_db, engine
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# User

@app.post("/api/users/signup", tags=["User"])
async def create_user_signup(user: schemas.UserCreate = Body(...), db: Session= Depends(get_db)):
    try:
        crud.create_user(db, user)
        return signJWT(user.email)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.post("/api/users/login", tags=["User"])
async def user_login(user: schemas.UserLoginSchema = Body(...), db: Session= Depends(get_db)):
    if crud.check_user(db, user):
        return signJWT(user.email)
    return {
        "error": "E-mail ou senha incorretos!"
    }

@app.get("/api/users/{user_id}",  tags=["User"], response_model=schemas.User, dependencies=[Depends(JWTBearer())])
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_user_by_id(db, user_id)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/api/users", tags=["User"], response_model=schemas.PaginatedUser, dependencies=[Depends(JWTBearer())] )
def get_all_users(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_users = crud.get_all_users(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_users}
    return response

@app.put("/api/users/{user_id}", tags=["User"], response_model=schemas.User, dependencies=[Depends(JWTBearer())] )
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_user(db, user_id, user)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/users/{user_id}", tags=["User"], dependencies=[Depends(JWTBearer())] )
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_user_by_id(db, user_id)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)

# Category

@app.get("/api/categories", tags=["Category"], response_model=schemas.PaginatedCategory, dependencies=[Depends(JWTBearer())])
def get_all_categories(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_categories = crud.get_all_categories(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_categories}
    return response


@app.get("/api/categories/{category_id}",  tags=["Category"], response_model=schemas.Category, dependencies=[Depends(JWTBearer())])
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_category_by_id(db, category_id)
    except CategoryException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.post("/api/categories", tags=["Category"], dependencies=[Depends(JWTBearer())])
async def create_category(category: schemas.CategoryBase = Body(...), db: Session= Depends(get_db)):
    try:
        return crud.create_category(db, category)
    except CategoryException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/categories/{category_id}", tags=["Category"], response_model=schemas.Category, dependencies=[Depends(JWTBearer())] )
def update_category(category_id: int, category: schemas.CategoryBase, db: Session = Depends(get_db)):
    try:
        return crud.update_category(db, category_id, category)
    except CategoryException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/categories/{category_id}", tags=["Category"], dependencies=[Depends(JWTBearer())] )
def delete_category_by_id(category_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_category_by_id(db, category_id)
    except CategoryException as cie:
        raise HTTPException(**cie.__dict__)

# Accounts
@app.get("/api/accounts/{account_id}",  tags=["Account"], response_model=schemas.Account, dependencies=[Depends(JWTBearer())])
def get_account_by_id(account_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_account_by_id(db, account_id)
    except AccountException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.post("/api/accounts", tags=["Account"], dependencies=[Depends(JWTBearer())])
async def create_account(account: schemas.AccountBase = Body(...), db: Session= Depends(get_db)):
    try:
        return crud.create_account(db, account)
    except AccountException as cie:
        raise HTTPException(**cie.__dict__)

@app.put("/api/accounts/{account_id}", tags=["Account"], response_model=schemas.Account, dependencies=[Depends(JWTBearer())] )
def update_account(account_id: int, account: schemas.AccountBase, db: Session = Depends(get_db)):
    try:
        return crud.update_account(db, account_id, account)
    except AccountException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/api/accounts/{account_id}", tags=["Account"], dependencies=[Depends(JWTBearer())] )
def delete_account_by_id(account_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_account_by_id(db, account_id)
    except AccountException as cie:
        raise HTTPException(**cie.__dict__)