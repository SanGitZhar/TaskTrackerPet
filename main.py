from fastapi import FastAPI
from app.api.v1.task import router as task_router
from app.api.v1.users import router as users_router
from app.database import Base, engine

app = FastAPI()

@app.get("/tasks/{item_id}")
def get_all_tasks(item_id):
    return {"item_id": item_id}

app.include_router(task_router, prefix="/api/v1", tags=["task"])
app.include_router(users_router, prefix="/api/v1", tags=["users"])

Base.metadata.create_all(bind=engine)