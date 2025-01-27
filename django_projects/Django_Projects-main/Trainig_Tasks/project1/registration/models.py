from django.db import models

class UserRegistration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    objects = models.manager


class Meta:
     db_table  = "user table"
