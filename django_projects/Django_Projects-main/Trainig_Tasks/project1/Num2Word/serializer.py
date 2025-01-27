from rest_framework import serializers
from .models import word_models
from num2words import num2words

def convert(c):
    word = num2words(c)
    return word


class NumSerializer(serializers.ModelSerializer):
    class Meta:
        model = word_models
        fields = ["number", "num2word"]


    def create(self, validated_data):
        num = validated_data["number"]
        n2w = convert(num)
        print(n2w)
        user = word_models.objects.create(number=num, num2word=n2w)
        user.save()
        return user
