from django.db import models

class Binary(models.Model):
    image = models.CharField(max_length=200)
