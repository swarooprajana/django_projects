from rest_framework import serializers
from .models import stamp_models
import datetime


class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = stamp_models
        fields = ["present_time", "name", "age", "phone"]


    def create(self, validated_data):
        time = datetime.datetime.now()
        print(time)
        user = stamp_models.objects.create(name=validated_data["name"], age=validated_data["age"], phone=validated_data["phone"], present_time=time)
        user.save()
        return user
