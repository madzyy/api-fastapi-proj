from fastapi import FastAPI

# from passlib.context import CryptContext

import database
# from .database import SessionLocal,engine
# from . import models
import models
import routers.post
import routers.user
import routers.auth
import routers.vote


# pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
# models.Base.metadata.create_all(bind=database.engine)


models.database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()


my_posts = [{"title":"most expensive houses", "content":"these are the most expensive houses", "id":1},{"title":"most expensive cars", "content":"these are the most expensive cars", "id":2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


app.include_router(routers.post.router)
app.include_router(routers.user.router)
app.include_router(routers.auth.router)
app.include_router(routers.vote.router)

# @app.get("/")
# async def root():
#     return{"message":"Hello World!!!"}


