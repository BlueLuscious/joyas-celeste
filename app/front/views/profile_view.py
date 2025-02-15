import logging
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.backends.django import Template
from django.views import View

logger = logging.getLogger(__name__)


class ProfileView(View):

    """ View for `profile.html` template. """

    def get(self, request: HttpRequest) -> HttpResponse:
        template: Template = loader.get_template("pages/profile.html")
        logger.info(f"Current template: {template.template.name}")
        return HttpResponse(template.render(None, request))
    