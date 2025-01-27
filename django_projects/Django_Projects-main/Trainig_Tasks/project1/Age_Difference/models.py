from django.db import models
from datetime import date
from datetime import datetime



class Age_difference(models.Model):
    dob1 = models.DateField()
    dob2 = models.DateField()
    age = models.IntegerField()
    objects = models.manager

class Meta:
    db_table = "table"
