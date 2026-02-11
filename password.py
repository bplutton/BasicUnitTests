def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True