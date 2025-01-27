from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    objects = models.manager
