from functions.get_service import get_tasks_service
from responses.response_json import response_json

service = get_tasks_service()

def get_tasks(tasklist_id: str):
    try:
        response = service.tasks().list(tasklist=tasklist_id).execute()
        return response_json("Tasks retrieved successfully", response)
    except Exception as e:
        return response_json(message=str(e), status=500)

def create_task(tasklist_id: str, task: dict):
    try:
        response = service.tasks().insert(tasklist=tasklist_id,body=task).execute()
        return response_json("Task created successfully", response)
    except Exception as e:
        return response_json(message=str(e), status=500)

def get_task(tasklist_id: str, task_id: str):
    try:
        response = service.tasks().get(tasklist=tasklist_id, task=task_id).execute()
        return response_json("Task retrieved successfully", response)
    except Exception as e:
        return response_json(message=str(e), status=500)

def delete_task(tasklist_id: str, task_id: str):
    try:
        response = service.tasks().delete(tasklist=tasklist_id, task=task_id).execute()
        return response_json("Task deleted successfully", response)
    except Exception as e:
        return response_json(message=str(e), status=500)

def update_task(tasklist_id: str, task_id: str, task: dict):
    try:
        # Ensure the task_id and tasklist_id are being used correctly
        response = service.tasks().update(tasklist=tasklist_id, task=task_id, body=task).execute()
        print(response)  # For debugging purposes
        return response_json("Task updated successfully", response)
    except Exception as e:
        print(f"Error updating task: {e}")  # For debugging purposes
        return response_json(message=str(e), status=500)


# functions/tasks.py

def list_task_lists():
    try:
        response = service.tasklists().list().execute()
        return response_json("Task lists retrieved successfully", response)
    except Exception as e:
        return response_json(str(e), status=500)
