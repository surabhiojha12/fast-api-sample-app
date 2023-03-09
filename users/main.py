from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Users"}

@app.get("/users")
def read_users():
    return []

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}    

@app.get("/users/{user_id}/orders")
def read_user(user_id: int):
    return {"user_id": user_id, "orders": []}
