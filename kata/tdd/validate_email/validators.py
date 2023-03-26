import re

def is_email(value):
    """Verify if given value is a valid email address

    Args:
        value (str): Value to inspect

    Returns:
        bool: Returns True if value is a valid email address and False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'

    regex = re.compile(pattern)
    match = regex.search(value)

    return bool(match)
