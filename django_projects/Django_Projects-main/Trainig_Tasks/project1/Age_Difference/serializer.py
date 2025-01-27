from .models import Age_difference
from rest_framework import serializers
from datetime import date
from datetime import datetime


class DiffernceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Age_difference
        fields = ["dob1", "dob2"]

#
# def diff(dob3, dob4):
#     age = (dob3.year-dob4.year)
#     n = age.save()
#


# class SaveSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Age_difference
#         fields = ["dob1", "dob2"]



