from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from ._base import UserRepository
from .. import exceptions, schemas, models


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.UserCreate) -> schemas.User:
        if (
            self.db.query(models.User)
            .filter(models.User.username == user.username)
            .first()
        ):
            raise exceptions.AlreadyExists(
                exceptions.ERR_USER_ALREADY_EXISTS.format(username=user.username)
            )
        user_model = models.User(**user.dict())
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return schemas.User(**user_model.__dict__)

