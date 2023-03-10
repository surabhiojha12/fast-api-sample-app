from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    ph_no: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Users"}

@app.get("/health")
async def health():
    return {"message": "I am alive"}    

@app.get("/users")
async def read_users():
    return []

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}    

@app.post("/users")
async def create_user(user: User):
    return user
