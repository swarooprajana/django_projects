from django.db import models


class file_models(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    objects = models.manager



