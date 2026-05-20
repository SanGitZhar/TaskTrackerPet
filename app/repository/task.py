from sqlalchemy.orm import Session

from app.enum import TaskStatus
from app.models import User, Task

def create_task(db: Session, current_user: User, task_title: str, task_description: str, task_status: TaskStatus) -> Task:
    task = Task(title=task_title, description=task_description, status = task_status, user_id=current_user)
    db.add(task)
    db.flush()
    return task

def is_task_exist(db:Session, current_user: User, task_id) -> bool:
    return db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first is not None

def get_task(db: Session, current_user: User, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).scalar