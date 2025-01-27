from django.db import models
from django.core.validators import RegexValidator


class password_validation(models.Model):
     username = models.CharField(max_length=20)
     pwd = RegexValidator(regex="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{8,20}$",
                        message="must contain 6 letters and a capital letters and a special characters")
     password = models.CharField(validators=[pwd], max_length=20)
     objects = models.manager


class Meta:
    db_table = "validation"



