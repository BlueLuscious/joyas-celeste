from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class ClientModel(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
    