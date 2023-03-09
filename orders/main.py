from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Orders"}

@app.get("/orders")
def read_users():
    return []

@app.get("/orders/{order_id}")
def read_user(order_id: int):
    return {"order_id": order_id}    

@app.get("/orders/{order_id}/user")
def read_user(order_id: int):
    return {"order_id": order_id, "user": {}}
