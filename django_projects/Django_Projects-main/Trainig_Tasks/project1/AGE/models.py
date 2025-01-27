from django.db import models
from datetime import datetime
from datetime import date


class Age(models.Model):
    date = models.DateField()
    objects = models.manager


class Meta:
    db_table = "AGE"






