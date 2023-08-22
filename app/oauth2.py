from jose import JWTError,jwt
from datetime import datetime,timedelta
import schemas
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import database
import models
import config

oath2_scheme = OAuth2PasswordBearer('login')

# SECRET_KEY
SECRET_KEY=config.settings.SECRET_KEY

# ALGORITHM
ALGORITHM=config.settings.ALGORITHM

# EXPIRATION_TIME
ACCESS_TOKEN_EXPIRE_MINUTES=config.settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oath2_scheme), db: Session=Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    token=verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user