from django.db import models

# Create your models here.

class ClientInfo(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    confirmation = models.CharField(max_length=32)
    conditions = models.CharField(max_length=500)
    birth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()