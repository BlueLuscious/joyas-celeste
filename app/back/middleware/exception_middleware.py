import logging
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from back.exceptions.custom_exception import CustomException

logger = logging.getLogger(__name__)


class ExceptionMiddleware:

    """ Middleware to process own exceptions. """

    def __init__(self, get_response) -> None:

        """ ExceptionMiddleware Initializer. """

        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> HttpResponse:
        response: HttpResponse = self.get_response(request)
        return response

    def process_exception(self, request: WSGIRequest, exception: CustomException) -> HttpResponseRedirect:
        if isinstance(exception, CustomException):
            logger.info(f"{exception.code}: {exception.log}")
            messages.error(request, exception.message)
            return redirect(exception.redirect)
        