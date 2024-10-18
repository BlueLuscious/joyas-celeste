import logging
from back.forms.sign_up_form import SignUpForm
from back.handlers.sign_up_exception_handler import SignUpExceptionHandler
from back.models.client_model import ClientModel
from back.services.client_service import ClientService
from back.services.sign_up_service import SignUpService
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View

logger = logging.getLogger(__name__)


class SignUpView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("sign-up.html")
        context = {
            "form": SignUpForm
        }
        return HttpResponse(template.render(context, request))
    
    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        form = SignUpForm(request.POST)
        sign_up_service = SignUpService(form)
        client_service = ClientService()

        try:
            validated_form: dict = sign_up_service.validate_form()
            user: ClientModel = client_service.create_client(validated_form)
            messages.success(request, "Registro exitoso")
            return HttpResponseRedirect("/login/")
        except Exception as e:
            SignUpExceptionHandler.handle_exception(request, e)
            return HttpResponseRedirect("/sign-up/")
        