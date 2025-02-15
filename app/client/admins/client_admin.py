from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.core.handlers.wsgi import WSGIRequest
from client.models.client_model import ClientModel


@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):

    """ Admin for ClientModel. """

    list_display = (
        "username",
        "first_name",
        "last_name",
        "uuid",
        "created_at",
        "updated_at",
    )
    ordering = (
        "-created_at",
    )
    search_fields = (
        "uuid",
        "username",
        "first_name",
        "last_name",
    )

    def save_model(self, request: WSGIRequest, obj: ClientModel, form, change) -> HttpResponseRedirect:

        """ 
        Overwrite save_model method.
        
        Actions:
            - Hashed password.
        """

        if form.cleaned_data.get("password") != form.initial.get("password"):
            obj.password = make_password(obj.password)
        return super().save_model(request, obj, form, change)
    