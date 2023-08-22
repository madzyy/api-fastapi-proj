from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
# from passlib.context import CryptContext
import database
import utils
# from .database import SessionLocal,engine
# from . import models
import models
import schemas
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=['Users']
)   

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db: Session=Depends(database.get_db)):
    # hashed_password = pwd_context.hash(user.password)
    hashed_password = utils.hash(user.password)
    user.password=hashed_password
    new_user = models.User(**user.dict()) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} is not found")
    return user
