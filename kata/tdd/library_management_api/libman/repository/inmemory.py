from ..models import User
from ..exceptions import AlreadyExists, ERR_USER_ALREADY_EXISTS, DoesNotExist, ERR_USER_DOES_NOT_EXISTS
from ._base import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def create_user(self, user: User):
        if user.username in self.users:
            raise AlreadyExists(ERR_USER_ALREADY_EXISTS.format(username=user.username))
        self.users[user.username] = user
        return user
    
    def get_user(self, username: str) -> User:
        if username not in self.users:
            raise DoesNotExist(ERR_USER_DOES_NOT_EXISTS.format(username=username))
        return self.users[username]
    
    def list_users(self):
        return list(self.users.values())
    
    def update_user(self, username: str, user: User):
        if username not in self.users:
            raise DoesNotExist(ERR_USER_DOES_NOT_EXISTS.format(username=username))
        self.users[username] = user
        return user
