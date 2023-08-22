# from .database import Base
import database
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(database.Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content=Column(String, nullable=False)
    published = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('NOW()'), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False)
    owner = relationship("User")

class User(database.Base):
    __tablename__ = "users"
    id = Column(Integer, nullable=False, primary_key=True)
    email = Column(String, nullable=False, unique=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('NOW()'), nullable=False) 

class Vote(database.Base):
    __tablename__="votes"
    user_id=Column(Integer, ForeignKey("users.id", ondelete="cascade"), primary_key=True)
    post_id=Column(Integer, ForeignKey("posts.id", ondelete="cascade"), primary_key=True)
