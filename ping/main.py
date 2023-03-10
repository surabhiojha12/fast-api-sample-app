from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import asyncio

class Order(BaseModel):
    id: int
    name: str
    user_id: int

app = FastAPI()

# since both containers are part of same network
URL = "http://user_container:8000/health"

@app.get("/")
async def root():
    return {"message": "Hello Monitor api"}

@app.get("/ping")
async def ping_users():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(URL)
            return { "status": response.status_code }
    except:
        return { "status": 503 }
