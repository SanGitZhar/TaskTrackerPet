from fastapi import FastAPI

app = FastAPI()

@app.get("/tasks")
def get_all_tasks():
    return {"message": "hello world"}