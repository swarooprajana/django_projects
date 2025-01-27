from django.db import models

class Encrypt(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    Roll_No = models.CharField(max_length=20)
    objects = models.manager

class Meta:
    db_table = "password_Encrypt"