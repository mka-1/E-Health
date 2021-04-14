from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    confirmation = models.CharField(max_length=32)
    conditions = models.CharField(max_length=500)
    birth = models.DateField()