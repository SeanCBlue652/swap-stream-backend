from fastapi import FastAPI
import dao

app = FastAPI() 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_item(user_id: int):
    return dao.get_userdata()

