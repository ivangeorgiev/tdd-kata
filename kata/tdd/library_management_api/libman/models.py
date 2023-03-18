from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Example in-memory data store for users
users = {}

# Define a user model using Pydantic
class User(BaseModel):
    username: str
    email: str
    password: str
    full_name: str = None

