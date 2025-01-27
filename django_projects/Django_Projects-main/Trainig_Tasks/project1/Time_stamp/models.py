from django.db import models


class stamp_models(models.Model):
    present_time = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    objects = models.manager


