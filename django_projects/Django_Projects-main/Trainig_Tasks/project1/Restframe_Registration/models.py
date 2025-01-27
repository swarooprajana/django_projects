from django.db import models

class UserRegistration(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    pin_no = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    objects = models.manager


class Meta:
    db_table = 'RF_Registration'
