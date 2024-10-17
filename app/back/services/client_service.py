import logging
from back.exceptions.sign_up_exception import (
    SignUpError, UserAlreadyExistsError
)
from back.forms.sign_up_form import SignUpForm
from back.models.client_model import ClientModel
from back.services.sign_up_service import SignUpService

logger = logging.getLogger(__name__)


class ClientService:

    @staticmethod
    def create_client(form: SignUpForm) -> ClientModel:

        """
        Create a ClientModel instance.

        Args:
            form (SignUpForm): form with registration data.

        Returns:
            ClientModel: ClientModel instance.
        """

        if form.is_valid():
            data: dict = form.cleaned_data
            password: str = data.pop('password')
            repeat_password: str = data.pop('repeat_password')

            password: str = SignUpService.validate_password(password, repeat_password)

            try:
                user = ClientModel.objects.create_user(password=password, **data)
                logger.info(f"User {user.username} was created")
                return user
            except Exception as e:
                raise SignUpError("Ocurrió un error inesperado") from e
        else:
            if form.errors.get("username"):
                raise UserAlreadyExistsError("Un usuario con este nombre ya existe")
            