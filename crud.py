from sqlalchemy.orm import Session
from exceptions import UserAlreadyExistError, UserNotFoundError
import bcrypt, models, schemas

# usuário
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
