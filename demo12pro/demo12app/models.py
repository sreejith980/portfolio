from django.db import models
# Create your models here.
class login(models.Model):
    name = models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    email=models.EmailField()
    yourmessage=models.TextField(max_length=500)
    