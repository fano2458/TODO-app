from model.model import Task, TaskList
import json
from pydantic import parse_file_as
from typing import List, Optional


filepath = "data/tasks.json"


async def data_to_json(data: List):
	pass


async def get_tasks(id: Optional[int]=0):
	return "response"


async def create_task(new_task: Task):
	return "id"


async def delete_task(id):
	return "id"


async def update_task(id: int, new_task: Task):
	return "id"