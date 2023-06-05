from django.db import models

# Create your models here.

class Login(models.Model):
    user_name = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    user_type = models.CharField(max_length=150)
    status=models.CharField(max_length=150)
