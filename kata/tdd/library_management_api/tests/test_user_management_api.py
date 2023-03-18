from http import HTTPStatus
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

from ..main import app, user_repository
from ..libman.models import User
from ..libman.repository import UserRepository
from ..libman.exceptions import AlreadyExists, DoesNotExist

test_user = User(
    username="testuser",
    email="testuser@example.com",
    password="password",
    full_name="Test User",
)
create_user = User(
    username="createduser",
    email="createduser@example.com",
    password="mypassword",
    full_name="my-name",
)
update_user = User(
    username="testuser",
    email="testuser@example.com",
    password="newpassword",
    full_name="Test User Updated",
)
invalid_user = {"username": "joe", "email": "joe@example.com"}


class MockUserRepository(UserRepository):
    def get_user(self, username: str):
        if username == "testuser":
            return test_user
        raise DoesNotExist(f"User '{username}' doesn't exist.")

    def list_users(self):
        return [test_user]


class UserAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        app.dependency_overrides[user_repository] = MockUserRepository


class TestGetUserAPI(UserAPITestCase):
    def test_can_call_get_user(self):
        self.assertIsNotNone(self.client)
        response = self.client.get("/users/testuser")
        self.assertEqual(response.status_code, 200)

    def test_should_return_existing_user(self):
        response = self.client.get("/users/testuser")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), test_user.dict())

    def test_should_return_NOT_FOUND_user_does_not_exist(self):
        response = self.client.get("/users/missing-user")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(), {"message": "User 'missing-user' doesn't exist."}
        )


class TestListUsersAPI(UserAPITestCase):
    def test_can_call_list_users(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)


class TestCreateUserAPI(UserAPITestCase):
    def test_should_create_user_using_repository(self):
        with patch.object(MockUserRepository, "create_user") as create_user_mock:
            response = self.client.post("/users/", json=create_user.dict())
            self.assertEqual(response.status_code, HTTPStatus.CREATED)
            self.assertEqual(response.json(), {"result": "OK"})
            create_user_mock.assert_called_once_with(create_user)

    def test_should_return_CONFLICT_user_already_exists(self):
        with patch.object(MockUserRepository, "create_user") as create_user_mock:
            create_user_mock.side_effect = AlreadyExists("User 'testuser' already exists.")
            response = self.client.post("/users/", json=update_user.dict())
            self.assertEqual(
                response.json(), {"message": "User 'testuser' already exists."}
            )

    def test_should_return_UNPROCESSABLE_ENTITY_invalid_user(self):
        response = self.client.post("/users/", json=invalid_user)
        self.assertEqual(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        expected_content = {
            "detail": [
                {
                    "loc": ["body", "password"],
                    "msg": "field required",
                    "type": "value_error.missing",
                }
            ]
        }
        self.assertEqual(response.json(), expected_content)


class TestUpdateUserAPI(UserAPITestCase):
    def test_should_update_existing_user_using_repository(self):
        with patch.object(MockUserRepository, "update_user") as update_user_mock:
            response = self.client.put(f"/users/{update_user.username}", json=update_user.dict())
            self.assertEqual(response.status_code, HTTPStatus.ACCEPTED)
            update_user_mock.assert_called_once_with(update_user.username, update_user)

    def test_should_return_NOT_FOUND_user_does_not_exist(self):
        with patch.object(MockUserRepository, "update_user") as update_user_mock:
            update_user_mock.side_effect = DoesNotExist(f"User 'testuser' doesn't exist.")
            response = self.client.put(f"/users/testuser", json=update_user.dict())
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
            self.assertEqual(response.json(), {"message": f"User 'testuser' doesn't exist."})
