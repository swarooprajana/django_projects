from django.db import models


class BMI_models(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    calculate_BMI = models.FloatField()
    objects = models.manager



