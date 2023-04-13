import abc
from .. import schemas

class UserRepository(abc.ABC):
    def create_user(self, user: schemas.UserCreate) -> schemas.User:
        """Add new user to the repository. Throws AlreadyExists exception if user already exists in the repository."""
        raise NotImplemented

    def get_user(self, username: str) -> schemas.User:
        """Retrieve user from the repository. Throws DoesNotExist exception if user doesn't exist in the repository."""
        raise NotImplemented

    def update_user(self, username: str, user: schemas.UserUpdate) -> schemas.User:
        """Replace the user details in the repository. Throws DoesNotExist exception if user doesn't exist in the repository."""
        raise NotImplemented

    def list_users(self) -> list[schemas.User]:
        """Get a list of all users from the repository."""
        raise NotImplemented

