from back.models.client_model import ClientModel
from django.contrib import admin


@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "uuid", "created_at", "updated_at", )
    ordering = ("-created_at", )
    search_fields = ("uuid", "username", "first_name", "last_name", )
