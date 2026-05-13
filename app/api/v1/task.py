from fastapi import APIRouter

from app.schemas import TaskResponse, CreateTaskRequest
from app.service import task as task_service

router = APIRouter

@router.post("/task", response_model=TaskResponse)
def create_task(task: CreateTaskRequest):
    return task_service.create_task(task)

@router.get("/task")
def get_task():
    pass