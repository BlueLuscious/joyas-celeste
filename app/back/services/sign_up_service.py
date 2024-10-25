import logging
from back.exceptions.sign_up_exception import (
    PasswordLengthError, PasswordMismatchError, UserAlreadyExistsError
)
from back.forms.sign_up_form import SignUpForm
from back.models.client_model import ClientModel
from django.http import QueryDict

logger = logging.getLogger(__name__)


class SignUpService:

    def __init__(self, form: SignUpForm) -> None:
        self.form = form

    
    def validate_form(self) -> dict:

        """ 
        Validate registration form.
        
        Returns:
            dict: Validated form data.
        """

        data: QueryDict = self.form.data

        username: str = data.get("username")
        username: str = self.validate_username(username)

        password: str = data.get("password")
        repeat_password: str = data.get("repeat_password")
        password: str = self.validate_password(password, repeat_password)

        if self.form.is_valid():
            validated_data: dict = self.form.cleaned_data
            validated_data.pop("repeat_password")
            logger.info(f"Validated form data successfully: {validated_data}")
        return validated_data


    def validate_username(self, username: str) -> str:

        """ 
        Validate username.

        Args:
            username (str): Username.
        
        Returns:
            str: Validated username.
        """

        if ClientModel.objects.filter(username=username).exists():
            raise UserAlreadyExistsError()
        
        logger.info(f"Validated username successfully: {username}")
        return username


    def validate_password(self, password: str, repeat_password: str) -> str:

        """ 
        Validate password.

        Args:
            password (str): Password.
            repeat_password (str): Repeated password.
        
        Returns:
            str: Validated password.
        """

        if not (6 < len(password) < 12):
            raise PasswordLengthError()
        if password != repeat_password:
            raise PasswordMismatchError()
        
        logger.info(f"Validated password successfully: {password}")
        return password
    