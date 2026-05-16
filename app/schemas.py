from pydantic import BaseModel, Field

from app.enum import TaskStatus


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

class UserRequest(BaseModel):
    login: str = Field(..., max_length=127)

class UserResponse(UserRequest):
    model_config = {"from_attributes": True}

    id: int