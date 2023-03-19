from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserCreate):
    pass

class User(UserBase):
    pass
