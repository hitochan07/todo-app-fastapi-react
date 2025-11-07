from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS設定（React側のポートを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydanticモデル定義
class Todo(BaseModel):
    id: int | None = None
    title: str
    description: str
    completed: bool = False

todos = [
    {"id": 1, "title": "Todo 1", "description": "Description 1", "completed": False}, 
    {"id": 2, "title": "Todo 2", "description": "Description 2", "completed": True}
]
next_id = 1

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: Todo):
    new_id = max(t["id"] for t in todos) + 1 if todos else 1
    todo.id = new_id
    todos.append(todo.dict())
    return todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: Todo):
    for t in todos:
        if t["id"] == todo_id:
            t["title"] = updated.title
            t["description"] = updated.description
            t["completed"] = updated.completed
            return t
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    for t in todos:
        if t["id"] == todo_id:
            todos = [x for x in todos if x["id"] != todo_id]
            return {"message": f"Todo {todo_id} deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")