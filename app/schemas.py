from typing import ForwardRef, List, Union

from pydantic import BaseModel

# Takes care of the classes referencing each other
User = ForwardRef("User")

class PostBase(BaseModel):
    title: str
    user_id: int
    content: Union[str, None]


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    events: List[Post] = []

    class Config:
        orm_mode = True

# Takes care of the classes referencing each other
Post.update_forward_refs()
