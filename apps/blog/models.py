from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Blog(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
