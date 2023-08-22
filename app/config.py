from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOSTNAME: str="localhost"
    DATABASE_PORT: str="5432"
    DATABASE_NAME: str="fastapi"
    DATABASE_USERNAME: str="postgres"
    DATABASE_PASSWORD: str="password123"
    SECRET_KEY: str="09423454345vwer324234g4543534f23423sdfr34453323435"
    ACCESS_TOKEN_EXPIRE_MINUTES: int=30
    ALGORITHM:str="HS256"

    class Config:
        env_file = ".env"

settings = Settings()