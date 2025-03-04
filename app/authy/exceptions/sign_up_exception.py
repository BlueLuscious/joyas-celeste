from app.exceptions.custom_exception import CustomException
from app.settings import SIGN_UP_PATH


class SignUpError(CustomException):
    
    """ Base exception for registration errors. """
    
    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "Ocurrió un error inesperado",
            "Sign Up Unexpected Error",
            SIGN_UP_PATH,
        )

class PasswordMismatchError(CustomException):
    
    """ Exception for mismatching passwords. """

    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "Las contraseñas no coinciden", 
            "Mismatching Passwords",
            SIGN_UP_PATH,
        )

class PasswordLengthError(CustomException):
    
    """ Exception for invalid password length. """
    
    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "La contraseña debe tener en 6 y 12 caracteres",
            "Invalid Password Length",
            SIGN_UP_PATH,
        )

class UserAlreadyExistsError(CustomException):

    """ Exception for existing user. """
    
    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "Un usuario con este nombre ya existe",
            "Existing User",
            SIGN_UP_PATH,
        )
        