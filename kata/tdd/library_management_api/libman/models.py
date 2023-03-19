
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    full_name = Column(String, default=None)
