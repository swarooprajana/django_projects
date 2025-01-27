from rest_framework import serializers
from .models import BMI_models



def calculate(h,w):
    BMI = w/(h/100)**2
    return BMI


class BMISerializer(serializers.ModelSerializer):
    class Meta:
        model = BMI_models
        fields = ["weight", "height", "calculate_BMI"]

    def create(self, validated_data):
        wei = validated_data["weight"]
        hei = validated_data["height"]
        calculate_BMI = calculate(wei, hei)
        print(calculate_BMI)
        user = BMI_models.objects.create(weight=wei, height=hei, calculate_BMI=calculate_BMI)
        user.save()
        return user


