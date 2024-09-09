from back.forms.sign_up_form import SignUpForm
from back.models.client_model import ClientModel
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.views import View


class SignUpView(View):
    def get(self, request):
        template = loader.get_template("sign-up.html")
        context = {
            "form": SignUpForm
        }
        return HttpResponse(template.render(context, request))
    
    def post(self, request):
        data = {
            "email": request.POST.get("username"),
            "username": request.POST.get("username"),
            "password": request.POST.get("password"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
        }

        ClientModel.objects.create_user(**data)
        return redirect("login")
    