from django.db import models
from django_countries.fields import CountryField
from datetime import datetime

class Currency(models.Model):
    country = CountryField(blank_label={'select your country_currency'})
    cou_currency = models.CharField(max_length=20)
    currency_symbol = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=True)
    objects = models.manager


class Meta:
    db_table = "Currency_table"
