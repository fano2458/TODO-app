from model.model import Task, TaskList
import json
from pydantic import parse_file_as
from typing import List, Optional


filepath = "data/tasks.json"


async def data_to_json(data: List):
	data = json.dumps(data)
	with open(filepath, "w") as file:
		file.write(data)


async def get_tasks(id: Optional[int]=0):
	tasks = parse_file_as(List[TaskList],"data/tasks.json")
	data = {task.id: task.dict() for task in tasks}
	try:
		response = data if id == 0 else data[id]
	except KeyError:
		response = data
	return response


async def create_task(new_task: Task):
	tasks = parse_file_as(List[TaskList],"data/tasks.json")
	id = max([task.id for task in tasks])+1
	tasks.append(TaskList(id=id,task=new_task))
	data = [task.dict() for task in tasks]
	await data_to_json(data)
	return id


async def delete_task(id):
	tasks = parse_file_as(List[TaskList],"data/tasks.json")
	tasks = [task for task in tasks if task.id != id]
	data = [task.dict() for task in tasks]
	await data_to_json(data)
	return id


async def update_task(id: int, new_task: Task):
	tasks = parse_file_as(List[TaskList],"data/tasks.json")
	data = [task.dict() for task in tasks]
	for task in data:
		if task["id"] == id:
			task["task"] = new_task.dict()
	await data_to_json(data)
	return id