from django.db import models



class Session(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=50)
    objects = models.manager


class Meta:
    db_table = "multi_session"


