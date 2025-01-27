from django.db import models


class word_models(models.Model):
    number = models.IntegerField()
    num2word = models.CharField(max_length=50)
    objects = models.manager

