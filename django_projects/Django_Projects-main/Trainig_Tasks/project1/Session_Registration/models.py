from django.db import models

class Registration(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    objects = models.manager


class Meta:
    db_table = "Session"