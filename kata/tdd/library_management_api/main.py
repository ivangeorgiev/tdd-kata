from http import HTTPStatus
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse

from .libman import schemas
from .libman.schemas import User
from .libman.exceptions import AlreadyExists, DoesNotExist
from .libman.repository import UserRepository
from .libman.repository.inmemory import InMemoryUserRepository

app = FastAPI()

user_repository_instance = InMemoryUserRepository()
def user_repository():
    return user_repository_instance

@app.exception_handler(DoesNotExist)
async def handle_does_not_exist_exception(request: Request, exc: DoesNotExist):
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={"message": str(exc)},
    )

@app.exception_handler(AlreadyExists)
async def handle_already_exists_exception(request: Request, exc: AlreadyExists):
    return JSONResponse(
        status_code=HTTPStatus.CONFLICT,
        content={"message": str(exc)},
    )


@app.post("/users/")
async def create_user(user: schemas.UserCreate, user_repository:UserRepository=Depends(user_repository)):
    user_repository.create_user(user)
    return JSONResponse(status_code=HTTPStatus.CREATED, content={"result": "OK"})

@app.get("/users/{username}")
async def get_user(username: str, user_repository:UserRepository=Depends(user_repository)):
    return user_repository.get_user(username)

@app.get("/users/")
async def list_users(user_repository:UserRepository=Depends(user_repository)):
    return user_repository.list_users()

@app.put("/users/{username}")
async def update_user(username: str, user: schemas.UserUpdate, user_repository:UserRepository=Depends(user_repository)):
    user_repository.update_user(username, user)
    return JSONResponse(status_code=HTTPStatus.ACCEPTED, content={"result": "ACCEPTED"})
