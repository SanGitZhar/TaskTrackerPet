from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User, Task
from app.schemas import CreateTaskRequest, TaskResponse
from app.repository import task as task_repository

def create_task(db: Session, current_user: User, task: CreateTaskRequest) -> TaskResponse:
    # if task_repository Is_task exist return httpexception 400 alredy exist

    #create new task
    task = task_repository.create_task(db, current_user.id, task.title, task.description, task.status)
    db.commit()
    return TaskResponse.model_validate(task)

def get_task(db: Session, current_user: User, task_id: int) -> TaskResponse | None:
    if task_repository.is_task_exist(db,current_user, task_id):
        raise HTTPException(status_code=404, detail=f"Task id '{task_id}' not found")
    result = task_repository.get_task(db, current_user, task_id)
    return TaskResponse.model_validate(result)

#Доделать получение тасков