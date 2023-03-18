ERR_USER_ALREADY_EXISTS = "User '{username}' already exists."
ERR_USER_DOES_NOT_EXISTS = "User '{username}' does not exist."

class AlreadyExists(Exception):
    pass

class DoesNotExist(Exception):
    pass
