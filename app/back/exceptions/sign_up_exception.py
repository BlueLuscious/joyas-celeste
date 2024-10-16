class SignUpError(Exception):
    """
    Base exception for registration errors.
    """

    def __init__(self, message: str, code: str = None) -> None:
        self.message = message
        self.code = code
        super().__init__(message)

class PasswordMismatchError(SignUpError):
    """
    Exception for mismatching passwords.
    """
    pass

class PasswordLengthError(SignUpError):
    """
    Exception for invalid password length.
    """
    pass

class UserAlreadyExistsError(SignUpError):
    """
    Exception for existing user.
    """
    pass
