from django.db import models

# Create your models here.
class Raiting(models.Model):
  user_id = models.BigIntegerField()
  r_count = models.IntegerField()
  r_score = models.DecimalField(max_digits=4, decimal_places=2)