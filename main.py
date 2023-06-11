from fastapi import FastAPI
from datetime import datetime
from typing import Optional

from fasapi.encoders import jsonable_encoder
from model.model import Task, TaskList
import model.taskman as taskman


app = FastAPI()


@app.get("/api/tasks")
async def get_tasks():
	return "TODO"


@app.get("api/tasks/{id}")
async def get_task(id: int):
	return "TODO"


@app.post("/api/tasks/create")
async def create_task(task: Task):
	return "TODO"


@app.put("/api/tasks/{id}/update")
async def update_task(id: int, task: Task):
	return "TODO"


@app.delete("/api/tasks/{id}/delete")
async def delete_task(id: int):
	return "TODO"