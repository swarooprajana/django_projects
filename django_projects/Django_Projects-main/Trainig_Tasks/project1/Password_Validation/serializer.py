from rest_framework import serializers
from .models import password_validation


class ValidatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = password_validation
        fields = '__all__'
