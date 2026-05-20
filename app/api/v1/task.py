from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import TaskResponse, CreateTaskRequest
from app.service import task as task_service
from app.dependency import get_db, get_current_user

router = APIRouter()

@router.post("/task", response_model=TaskResponse)
def create_task(task: CreateTaskRequest, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    return task_service.create_task(db, current_user, task)

@router.get("/task", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.get_task(db, current_user, task_id)
#Доделать
# @router.get("/task", response_model=list[TaskResponse])
# def get_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return task_service.get_task(db, current_user, task_id)
# #Доделать