import logging
from back.exceptions.sign_up_exception import (
    PasswordLengthError, PasswordMismatchError
)

logger = logging.getLogger(__name__)


class SignUpService:

    @staticmethod
    def validate_password(password: str, repeat_password: str) -> str:

        """ 
        Validate password.

        Args:
            password (str): password.
            repeat_password (str): repeated password.
        
        Returns:
            str: validated password.
        """

        if password != repeat_password:
            raise PasswordMismatchError("Las contraseñas no coinciden")
        if not (6 < len(password) < 12):
            raise PasswordLengthError("La contraseña debe tener en 6 y 12 caracteres")
        
        return password
    