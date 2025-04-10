from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    