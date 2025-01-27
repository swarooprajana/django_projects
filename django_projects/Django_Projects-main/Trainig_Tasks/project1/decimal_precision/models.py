from django.db import models


class Decimal(models.Model):
    number = models.FloatField()
    digits = models.IntegerField()
    decimal_value = models.FloatField()
    objects = models.manager
