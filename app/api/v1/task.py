from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class CreateTaskRequest(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.PENDING
    #date_created, deadline,

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None=None
    description: TaskStatus
    #date_created, deadline,
    class Config():
        from_attributes = True

    

router = APIRouter

@router.post("/task", response_model=TaskResponse)
def create_task(task: CreateTaskRequest):
    pass

@router.get("/task")
def get_task():
    pass