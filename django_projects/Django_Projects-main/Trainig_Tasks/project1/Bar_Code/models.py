from django.db import models
import barcode


class BarCode(models.Model):
    item_name = models.CharField(max_length=30)
    item_code = models.CharField(max_length=30)
    pack_code = models.CharField(max_length=30)
    bar_code = models.CharField(max_length=100)
    objects = models.manager
