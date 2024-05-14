import logging
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.views import View


class IndexView(View):
    def get(self, request):
        template = loader.get_template("index.html")
        return HttpResponse(template.render(None, request))
