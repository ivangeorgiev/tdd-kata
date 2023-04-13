import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...libman import models, schemas, exceptions
from ...libman.repository import UserRepository
from ...libman.repository.sqlalchemy import SqlAlchemyUserRepository

existing_user_dict = dict(
    username="testuser",
    email="testuser@example.com",
    password="password",
    full_name="Test User",
)

create_user = schemas.UserCreate(
    username="createduser",
    email="createduser@example.com",
    password="mypassword",
    full_name="my-name",
)


class TestSqlAlchemyUserRepository_init(unittest.TestCase):
    def test_constructor_should_return_UserRepository(self):
        repository = SqlAlchemyUserRepository('sqlite:///:memory:')
        self.assertIsInstance(repository, UserRepository)

class TestSqlAlchemyUserRepository_create_user(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        self.SessionLocal = sessionmaker(bind=engine)
        self.db = self.SessionLocal()
        models.BaseModel.metadata.create_all(bind=engine)
        user = models.User(**existing_user_dict)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        self.repository = SqlAlchemyUserRepository(self.db)

    
    def test_should_create_user(self):
        self.repository.create_user(create_user)

        saved_user = self.db.query(models.User).filter(models.User.username == 'createduser').first()
        
        self.assertEqual(saved_user.id, 2)
        self.assertEqual(schemas.UserCreate(**saved_user.__dict__), create_user)

    def test_should_return_User_schema(self):
        result = self.repository.create_user(create_user)
        
        self.assertIsInstance(result, schemas.User)
        self.assertEqual(result, schemas.User(**create_user.dict()))

    def test_should_raise_AlreadyExists_user_aready_exists(self):
        duplicate_user = schemas.UserCreate(**existing_user_dict)
        with self.assertRaises(exceptions.AlreadyExists) as exc:
            self.repository.create_user(duplicate_user)
        expected_exception_message = exceptions.ERR_USER_ALREADY_EXISTS.format(username='testuser')
        self.assertEqual(str(exc.exception), expected_exception_message)
