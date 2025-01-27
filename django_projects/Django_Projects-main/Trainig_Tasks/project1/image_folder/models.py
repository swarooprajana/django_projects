from django.db import models

class image(models.Model):
    images = models.ImageField()
    objects = models.manager


class Meta:
    db_table = "folder"

