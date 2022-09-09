from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, Session

from .database import Base, engine


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    posts = relationship("Post")


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String(256), nullable=False)
    content = Column(Text)
