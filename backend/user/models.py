from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=254)
  email = models.CharField(max_length=254)
  password = models.CharField(max_length = 256)
  date = models.DateField(auto_now_add=True) # should be set to date at creation of object automatically