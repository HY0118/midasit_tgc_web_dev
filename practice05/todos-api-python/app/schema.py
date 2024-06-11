from pydantic import BaseModel

class TodoBase(BaseModel):
    id: int
    content: str
    done: bool

class TodoCreate(BaseModel):
    content: str
    done : bool

class TodoUpdate(BaseModel):
    id: int
    content: str
    done : bool

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True