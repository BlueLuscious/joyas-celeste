from django.db import models
from typing import TYPE_CHECKING
from uuid import uuid4
if TYPE_CHECKING:
    from django.db.models import QuerySet
    from product.models.product_variation_model import ProductVariationModel


class MeasureModel(models.Model):

    """
    Measure Model.

    Fields:
        uuid (UUID): Unique Universal Identifier.
        size (str): Measure size.
        milimeters (str): Measure in milimeters.
        description (str): A description.
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.

    Related Fields:
        variations (QuerySet[ProductVariationsModel]): ProductVariationModel Instances. 
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    size = models.CharField(max_length=128)
    milimeters = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    variations: "QuerySet[ProductVariationModel]"


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Measure size.
        """

        return self.size
