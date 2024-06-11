from sqlalchemy.orm import Session
from app.models import Todo
from app.schema import TodoCreate
from app.schema import TodoUpdate

def get_todos(db: Session):
    return db.query(Todo).all()

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(**todo.dict())
    db.add(db_todo)
    db.commit()

def update_todo(db: Session, todo: Todo, updated_todo: TodoUpdate):
    for key, value in updated_todo.dict().items():
        setattr(todo, key, value)
    db.commit()

def delete_todo(db: Session, todo: Todo):
    db.delete(todo)
    db.commit()