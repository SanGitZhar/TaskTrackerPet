from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import CreateTaskRequest, TaskResponse
from app.repository import task as task_repository

def create_task(db: Session, current_user: User, task: CreateTaskRequest) -> TaskResponse:
    # if task_repository Is_task exist return httpexception 400 alredy exist

    #create new task
    task = task_repository.create_task(db, current_user.id, task.title, task.description, task.status)
    db.commit()
    return TaskResponse.model_validate(task)