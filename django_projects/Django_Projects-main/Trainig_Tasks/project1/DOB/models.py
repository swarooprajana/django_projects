from django.db import models
from datetime import date
from datetime import datetime


class DOB(models.Model):
    Age = models.IntegerField()
    objects = models.manager


class Meta:
    db_table = "dob"
