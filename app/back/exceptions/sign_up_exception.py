from back.exceptions.custom_exception import CustomException

SIGN_UP_REDIRECT = "sign-up"


class SignUpError(CustomException):
    
    """ Base exception for registration errors. """
    
    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "Ocurrió un error inesperado",
            "Sign Up Unexpected Error",
            SIGN_UP_REDIRECT,
        )

class PasswordMismatchError(CustomException):
    
    """ Exception for mismatching passwords. """

    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "Las contraseñas no coinciden", 
            "Mismatching Passwords",
            SIGN_UP_REDIRECT,
        )

class PasswordLengthError(CustomException):
    
    """ Exception for invalid password length. """
    
    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "La contraseña debe tener en 6 y 12 caracteres",
            "Invalid Password Length",
            SIGN_UP_REDIRECT,
        )

class UserAlreadyExistsError(CustomException):

    """ Exception for existing user. """
    
    def __init__(self, log: str) -> None:
        super().__init__(
            log,
            "Un usuario con este nombre ya existe",
            "Existing User",
            SIGN_UP_REDIRECT,
        )
        