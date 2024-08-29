from django.db import models
from django.utils.text import slugify
from uuid import uuid4


class SubcategoryModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, editable=False, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            slug = slugify(self.name)
            if SubcategoryModel.objects.filter(slug=slug).exists():
                unique_id = str(self.uuid)[:8]
                slug = f"{slug}-{unique_id}"
            self.slug = slug
        super(SubcategoryModel, self).save(*args, **kwargs)
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "slug"], name="subcategory_name_slug")
        ]
