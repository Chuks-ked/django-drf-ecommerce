from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Brand(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)