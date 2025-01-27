from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=30)
    college = models.CharField(max_length=50)
    objects = models.manager


class Meta:
    db_table = "serializer table"

