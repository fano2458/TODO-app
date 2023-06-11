from pydantic import BaseModel
from typing import NewType


ID = NewType("id", int)


class Task(BaseModel):
	summary: str
	priority: int


class TaskList(BaseModel):
	id: ID
	task: Task
