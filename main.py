from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from functions.calendar import create_task, delete_task, get_task, update_task, get_tasks
from routes.calendar import routes_tasks

app = FastAPI()

def custom_openapi():
    return get_openapi(
        title="google calender Backend API",
        description="API for google Backend",
        version="1.0.0",
        routes=app.routes,
    )

app.openapi = custom_openapi

app.include_router(routes_tasks, prefix="/calendar")
