from django.db import models

# Create your models here.
from django.db import models

class Shop(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  subcategory = models.CharField(max_length=255)
  amount = models.CharField(max_length=255)