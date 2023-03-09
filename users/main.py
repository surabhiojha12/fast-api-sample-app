from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    user_id: int

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Users"}

@app.get("/health")
def health():
    return {"message": "I am alive"}    

@app.get("/users")
def read_users():
    return []

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}    

@app.get("/users/{user_id}/orders")
def read_user(user_id: int):
    # TODO - make call to other service
    return {"user_id": user_id, "orders": []}
