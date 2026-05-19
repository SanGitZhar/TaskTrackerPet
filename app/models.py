from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from app.enum import TaskStatus
from app.database import Base

class User(Base):

    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)


class Task(Base):

    __tablename__ = "task"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None] = mapped_column(default=None)
    status: Mapped[TaskStatus]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)