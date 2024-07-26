from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from functions.calendar import create_task, get_tasks, get_task, delete_task, update_task, list_task_lists
from responses.response_json import response_json
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import Field


routes_tasks = APIRouter()

class TaskBody(BaseModel):
    title: str
    notes: Optional[str] = None  # For task description and any additional notes
    due: Optional[str] = None  # Due date/time in ISO 8601 format (UTC)
    completed: Optional[str] = None  # Completion date/time in ISO 8601 format (UTC)
    parent: Optional[str] = None  # ID of the parent task (if any)
    status: str = Field(..., description="Task status. Valid values: 'needsAction', 'completed'")
    start: Optional[str] = None  # Start date/time in ISO 8601 format (UTC)
    location: Optional[str] = None  # Location related to the task


@routes_tasks.get("/tasklists")
def list_tasklists():
    response = list_task_lists()
    
    if 'status_code' in response and response['status_code'] == 500:
        raise HTTPException(status_code=500, detail=response.get('message', 'Internal Server Error'))
    
    return JSONResponse(content=response, status_code=200)

@routes_tasks.post("/create")
async def create(tasklist_id: str, task: TaskBody):
    task_data = task.dict()
    response = create_task(tasklist_id,task_data)
    
    if 'status_code' in response and response['status_code'] == 500:
        raise HTTPException(status_code=500, detail=response.get('message', 'Internal Server Error'))
    
    return JSONResponse(content=response, status_code=200)

@routes_tasks.get("/tasks/{tasklist_id}")
def list_tasks(tasklist_id: str):
    response = get_tasks(tasklist_id)
    
    if 'status_code' in response and response['status_code'] == 500:
        raise HTTPException(status_code=500, detail=response.get('message', 'Internal Server Error'))
    
    return JSONResponse(content=response, status_code=200)

@routes_tasks.get("/task/{tasklist_id}/{task_id}")
def get(tasklist_id: str, task_id: str):
    response = get_task(tasklist_id, task_id)
    
    if 'status_code' in response and response['status_code'] == 500:
        raise HTTPException(status_code=500, detail=response.get('message', 'Internal Server Error'))
    
    return JSONResponse(content=response, status_code=200)

@routes_tasks.delete("/task/{tasklist_id}/{task_id}")
def delete(tasklist_id: str, task_id: str):
    response = delete_task(tasklist_id, task_id)
    
    if 'status_code' in response and response['status_code'] == 500:
        raise HTTPException(status_code=500, detail=response.get('message', 'Internal Server Error'))
    
    return JSONResponse(content=response, status_code=200)

@routes_tasks.put("/task/{tasklist_id}/{task_id}")
async def update(tasklist_id: str, task_id: str, task: TaskBody):
    task_data = task.dict()
    print(task_id)
    # Ensure the task_id is included in the request
    if not task_id:
        raise HTTPException(status_code=400, detail="Task ID is required")

    response = update_task(tasklist_id,task_id,task_data)

    # Check if the response indicates an error
    if isinstance(response, dict) and 'status_code' in response and response['status_code'] == 500:
        raise HTTPException(status_code=500, detail=response.get('message', 'Internal Server Error'))
    
    return JSONResponse(content=response, status_code=200)
