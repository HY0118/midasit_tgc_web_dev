from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255))
    done = Column(Boolean)