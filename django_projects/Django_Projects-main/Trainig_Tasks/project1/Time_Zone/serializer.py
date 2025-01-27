import pytz
from pytz import country_timezones
import datetime
import time
from .models import timezone
from rest_framework import serializers


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = timezone
        fields = ["TimeZone", "DateTime"]


    def create(self, validated_data):
        timezne = validated_data["TimeZone"]
        time = datetime.datetime.now(pytz.timezone(timezne))
        zon = timezone.objects.create(TimeZone=timezne, DateTime=time)
        zon.save()
        return zon



