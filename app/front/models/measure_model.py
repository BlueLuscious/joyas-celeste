from django.db import models
from uuid import uuid4


class MeasureModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    size = models.CharField(max_length=128)
    milimeters = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.size
