from pydantic import BaseModel


class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
    completed: bool
    user_id: int


class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
    completed: bool
    user_id: int


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str


class UpdateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str
