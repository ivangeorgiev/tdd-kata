from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a user model using Pydantic
class User(BaseModel):
    username: str
    email: str
    password: str
    full_name: str = None

# Example UserRepository interface with basic CRUD methods
class UserRepository:
    def __init__(self):
        self.users = {}

    def create_user(self, user: User):
        if user.username in self.users:
            raise HTTPException(status_code=400, detail="Username already registered")
        self.users[user.username] = user
        return user

    def get_user(self, username: str):
        if username not in self.users:
            raise HTTPException(status_code=404, detail="User not found")
        return self.users[username]

    def update_user(self, username: str, user: User):
        if username not in self.users:
            raise HTTPException(status_code=404, detail="User not found")
        self.users[username] = user
        return user

    def list_users(self):
        return list(self.users.values())

# Example in-memory UserRepository implementation
user_repository = UserRepository()

# Endpoint to create a new user
@app.post("/users/")
async def create_user(user: User):
    return user_repository.create_user(user)

# Endpoint to get a user by username
@app.get("/users/{username}")
async def get_user(username: str):
    return user_repository.get_user(username)

# Endpoint to update a user by username
@app.put("/users/{username}")
async def update_user(username: str, user: User):
    return user_repository.update_user(username, user)

# Endpoint to list all users
@app.get("/users/")
async def list_users():
    return user_repository.list_users()
