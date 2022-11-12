from django.db import models
from django.core.validators import FileExtensionValidator
from api.category.models import Category


class Product(models.Model):

    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    stock=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True,blank=True)
    image=models.ImageField(blank=True,null=True,upload_to="ProductIMG",validators=[FileExtensionValidator(allowed_extensions=["jpg","png","jpeg"])])
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
            return self.name


