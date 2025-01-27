import django as django
from rest_framework import serializers
#from models import logging
#django.db.models
from.models import logging


class LoggingSerializer(serializers.ModelSerializer):

     class Meta:
         model = logging
         fields = '__all__'

