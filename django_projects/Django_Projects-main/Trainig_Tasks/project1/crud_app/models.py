from django.db import models


class RegistrationModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    objects = models.manager


class Meta:
    db_table = "registration table"
