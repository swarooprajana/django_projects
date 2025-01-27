from django.db import models

class ForgetModels(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    objects = models.manager

