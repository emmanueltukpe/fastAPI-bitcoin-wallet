from typing import Union
import uvicorn
from fastapi import status as statuscode
from fastapi import FastAPI
from middleware import request_handler
from settings import api_settings as settings
from schemas.user_repo import UserRepository
from exceptions import *
from models import *


app = FastAPI()
app.middleware("http")(request_handler)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(
    "/signup",
    description="Create a new user",
    response_model=UserRead,
    status_code=statuscode.HTTP_201_CREATED,
    responses=get_exception_responses(PersonAlreadyExistsException),
    tags=["user"]
)
def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower()
    )
