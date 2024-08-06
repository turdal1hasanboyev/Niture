from django.db import models

import uuid
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.user.models import User
from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Banner(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to='banner/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Product(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=225)
    image = models.ImageField(upload_to="productimages/", null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name="products"
    )

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{uuid.uuid4()}"

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    @property
    def discount(self):
        if self.percentage:
            return self.price - (self.price * self.percentage) / 100
        
        return self.price
    
    @property
    def reviews_count(self):
        return self.rates.count()


class Review(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='rates')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = RichTextField(max_length=225, null=True, blank=True)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.message
