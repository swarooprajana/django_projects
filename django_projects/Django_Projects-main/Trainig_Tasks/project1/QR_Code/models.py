from django.db import models
import qr_code


class QR_Code(models.Model):
    product_name = models.CharField(max_length=20)
    product_code = models.CharField(max_length=20)
    pack_code = models.CharField(max_length=100)
    qr_code = models.CharField(max_length=100)
    objects = models.manager


class Meta:
    db_table = "table"