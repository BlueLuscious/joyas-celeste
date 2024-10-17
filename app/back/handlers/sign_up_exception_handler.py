import logging
from back.exceptions.sign_up_exception import (
    PasswordLengthError, PasswordMismatchError, 
    SignUpError, UserAlreadyExistsError
)
from django.contrib import messages
from django.http import HttpRequest

logger = logging.getLogger(__name__)


class SignUpExceptionHandler:
    
    @staticmethod
    def handle_exception(request: HttpRequest, exception: Exception) -> None:

        """
        Handle exceptions and log them.

        Args:
            request (HttpRequest): HttpRequest instance.
            exception (Exception): Any Exception instance.
        """

        if isinstance(exception, PasswordMismatchError):
            logger.error(f"Mismatching Passwords: {exception.message}")
            messages.error(request, exception.message)
        elif isinstance(exception, PasswordLengthError):
            logger.error(f"Invalid Password Length: {exception.message}")
            messages.error(request, exception.message)
        elif isinstance(exception, UserAlreadyExistsError):
            logger.error(f"Existing User: {exception.message}")
            messages.error(request, exception.message)
        elif isinstance(exception, SignUpError):
            logger.error(f"Sign Up Error: {exception.message}")
            messages.error(request, exception.message)
        else:
            logger.error("Unexpected Error")
            messages.error(request, "Ocurrió un error inesperado. Por favor, intenta nuevamente")
