import abc
from ..models import User

class UserRepository(abc.ABC):
    def create_user(self, user: User):
        """Add new user to the repository. Throws AlreadyExists exception if user already exists in the repository."""
        raise NotImplemented

    def get_user(self, username: str) -> User:
        """Retrieve user from the repository. Throws DoesNotExist exception if user doesn't exist in the repository."""
        raise NotImplemented

    def update_user(self, username: str, user: User):
        """Replace the user details in the repository. Throws DoesNotExist exception if user doesn't exist in the repository."""
        raise NotImplemented

    def list_users(self):
        """Get a list of all users from the repository."""
        raise NotImplemented

