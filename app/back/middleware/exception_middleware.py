import logging
from back.exceptions.custom_exception import CustomException
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


class ExceptionMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        response: HttpResponse = self.get_response(request)
        return response

    def process_exception(self, request: WSGIRequest, exception: CustomException) -> HttpResponseRedirect:
        if isinstance(exception, CustomException):
            logger.info(f"{exception.code}: {exception.message}")
            messages.error(request, exception.message)
            return redirect(exception.redirect)
        