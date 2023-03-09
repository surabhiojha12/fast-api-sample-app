from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import asyncio

class Order(BaseModel):
    id: int
    name: str
    user_id: int

app = FastAPI()

URL = "http://0.0.0.0:8000/health"

@app.get("/")
def root():
    return {"message": "Hello Monitor api"}

@app.get("/ping")
async def ping_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        return response.text
