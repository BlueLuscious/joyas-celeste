import logging
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


class LogOutView(LogoutView):

    """ View for log out. """

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        messages.success(request, "Cierre de sesión exitoso")
        return redirect("login")
    
        