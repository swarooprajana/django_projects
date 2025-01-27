import base64
from rest_framework import serializers
from .models import BarCode
import barcode
from .code import logic



class BarCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarCode
        fields = ["item_name", "item_code", "pack_code"]


    def create(self, validated_data):
        item_name = validated_data["item_name"]
        item_code = validated_data["item_code"]
        pack_code = validated_data["pack_code"]
        code_generation = item_code + " " + pack_code
        combine = logic(code_generation, item_name)
        with open(combine, 'rb') as img:
            encoded = base64.b64encode(img.read())
            print(encoded)
            name = BarCode.objects.create(item_name=item_name, item_code=item_code, pack_code=pack_code, bar_code=encoded)
            name.save()
            return name
