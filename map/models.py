from django.db import models

class Antenna(models.Model):
    name = models.CharField(max_length=100)
    configuration = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    status = models.CharField(max_length=10, default="up")

