from django.db import models


# Create your models here.
class DoctorInfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    usernameDr = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    confirmation = models.CharField(max_length=32)
    emailDr = models.CharField(max_length=60)
    specialization = models.CharField(max_length=500)
    hospital = models.CharField(max_length=100)
    dob = models.DateField()
