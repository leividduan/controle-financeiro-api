from fastapi import FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from exceptions import UserException
from database import get_db, engine
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

import crud, models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("api/users/signup", tags=["User"])
async def create_user_signup(user: schemas.UserCreate = Body(...), db: Session= Depends(get_db)):
    try:
        crud.create_user(db, user)
        return signJWT(user.email)
    except UserException as cie:
        raise HTTPException(**cie.__dict__)
    
@app.post("api/users/login", tags=["User"])
async def user_login(user: schemas.UserLoginSchema = Body(...), db: Session= Depends(get_db)):
    if crud.check_user(db, user):
        return signJWT(user.email)
    return {
        "error": "E-mail ou senha incorretos!"
    }

# usuário
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

#