from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=200,unique=True,null=False)
    name = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=30)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    password = models.IntegerField()
    content = models.TextField(max_length=500)


    class Meta:
        db_table = "login"