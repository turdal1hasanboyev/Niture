from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class SubEmail(BaseModel):
    email = models.EmailField(unique=True, null=True, blank=True, max_length=225)

    def __str__(self) -> str:
        return self.email
