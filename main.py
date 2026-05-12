from fastapi import FastAPI
from app.api.v1.task import router as task_router

app = FastAPI()

@app.get("/tasks/{item_id}")
def get_all_tasks(item_id):
    return {"item_id": item_id}

app.include_router(task_router, prefix="/api/v1", tags=["task"])
