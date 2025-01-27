from .models import DOB
from rest_framework import serializers


class DOBSerializer(serializers.ModelSerializer):

    class Meta:
        model = DOB
        fields = '__all__'
