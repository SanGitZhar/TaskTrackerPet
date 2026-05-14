from fastapi import HTTPException

from app.schemas import CreateTaskRequest, TaskResponse
from app.repository import task as task_repository

def create_task(task: CreateTaskRequest):
    # if task_repository Is_task exist return httpexception 400 alredy exist

    #create new task
    task = task_repository.create_task()
    return TaskResponse.model_validate(task)