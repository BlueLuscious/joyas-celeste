from django.db import models


class StatusOrderChoices(models.TextChoices):
    CANCELLED = "CANCELLED", "Cancelada"
    PENDING = "PENDING", "Pendiente"
    COMPLETED = "COMPLETED", "Completada"
