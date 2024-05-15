import logging
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.views import View

logger = logging.getLogger(__name__)

class IndexView(View):
    def get(self, request):
        template = loader.get_template("pages/index.html")
        logger.info(f"get template: {template.template.name}")
        return HttpResponse(template.render(None, request))
