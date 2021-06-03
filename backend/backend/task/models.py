from django.db import models

# Create your models here.
class Task(models.Model):
  requestor_id = models.BigIntegerField()
  description = models.TextField()
  date = models.DateField(auto_now_add=True)  # should be set to date at creation of object automatically
  acceptor_id = models.BigIntegerField(blank=True, null=True)
  title = models.CharField(max_length=50, blank=True, null=True)
  phone_number = models.CharField(max_length=16, blank=True, null=True)
  store_addr = models.CharField(max_length=100, blank=True, null=True)
  delivery_addr = models.CharField(max_length=100, blank=True, null=True)
  s_latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  s_longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  d_latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  d_longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
  
  #task types
  PHONE_CALL = 'PC'
  SUPPLIES = 'SP'
  OTHERS = 'OT'
  TYPES_CHOICES = [
    (PHONE_CALL, 'Phone Call'),
    (SUPPLIES, 'Supplies'),
    (OTHERS, 'others'),
  ]
  t_type = models.CharField(
    max_length=2,
    choices=TYPES_CHOICES,
    default=OTHERS)