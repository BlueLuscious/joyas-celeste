from back.models.client_model import ClientModel
from django.contrib import admin
from django.contrib.auth.hashers import make_password


@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
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

    def save_model(self, request, obj: ClientModel, form, change):
        if form.cleaned_data.get("password") != form.initial.get("password"):
            obj.password = make_password(obj.password)
        return super().save_model(request, obj, form, change)
    