import logging
from back.models.client_model import ClientModel
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.response import TemplateResponse

logger = logging.getLogger(__name__)


class LogInView(LoginView):

    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("registration/login.html")
        return HttpResponse(template.render(None, request))
    
    def form_valid(self, form: AuthenticationForm) -> TemplateResponse:
        messages.success(self.request, "Inicio de sesión exitoso")
        return super().form_valid(form)
        
    def form_invalid(self, form: AuthenticationForm) -> TemplateResponse:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = ClientModel.objects.filter(username=username).exists()
        if user:
            user = ClientModel.objects.get(username=username)
            checked_password = check_password(password, user.password)
            if not checked_password:
                logger.info(f"Wrong password")
                messages.error(self.request, "La contraseña es incorrecta")
        else:
            logger.info(f"User doesn't exist")
            messages.error(self.request, "El usuario es incorrecto")
        return super().form_invalid(form)
    