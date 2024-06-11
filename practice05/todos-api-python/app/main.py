from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app import crud, database, models, schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    database.create_tables()

@app.get("/")
async def root():
    return RedirectResponse(url="/todo/")

@app.get("/todo")
async def get_todos(db: Session = Depends(get_db)):
    todos = crud.get_todos(db)
    return todos


@app.put("/todo")
async def update_todo(updated_todo: schema.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, updated_todo.id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Fail to find todo")
    crud.update_todo(db, db_todo, updated_todo)

@app.post("/todo")
async def create_todo(todo: schema.TodoCreate, db: Session = Depends(get_db)):
    if not crud.create_todo(db, todo):
        raise HTTPException(status_code=404, detail="Invalid Start End Time")

@app.get("/DailyComment")
async def get_all_daily_comment(db: Session = Depends(get_db)):
    daily_comment = crud.get_all_daily_comment(db)
    return daily_comment

@app.post("/DailyComment")
async def create_daily_comment(daily_comment: schema.DailyCommentCreate, db: Session = Depends(get_db)):
    crud.create_daily_comment(db, daily_comment)

@app.get("/DailyComment/{date}")
async def get_daily_comment(date: int, db: Session = Depends(get_db)):
    daily_comment = crud.get_daily_comment(db, date)
    if daily_comment is None:
        raise HTTPException(status_code=404, detail="Fail to find daily comment")
    return daily_comment

@app.get("/todo/{todo_id}")
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo

@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    crud.delete_todo(db, db_todo)
    return {"message": "todo deleted successfully"}