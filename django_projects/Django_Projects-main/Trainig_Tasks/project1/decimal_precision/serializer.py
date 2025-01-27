from rest_framework import serializers
from .models import Decimal



def decimal(n, d):
    result = (round(n, d))
    print(result)
    return result


class DecimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decimal
        fields = ["number", "digits", "decimal_value"]


    def create(self, validated_data):
        number = validated_data["number"]
        digits = validated_data["digits"]
        decimal_value = decimal(number, digits)
        print('decimal_value')
        dec = Decimal.objects.create(number=validated_data["number"], digits=validated_data["digits"], decimal_value=decimal_value)
        dec.save()
        return dec


