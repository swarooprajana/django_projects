from django.db import models


class logging(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    objects = models.manager


class Meta:
    db_table = "LOGGING_TABLE"
