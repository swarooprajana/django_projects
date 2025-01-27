import base64
import pyqrcode
import png
from rest_framework import serializers
from .models import QR_Code



class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QR_Code
        fields = ["product_name", "product_code", "pack_code"]

    def create(self, validated_data):
        product_name = validated_data['product_name']
        product_code = validated_data['product_code']
        pack_code = validated_data['pack_code']
        add = product_code + " " + pack_code
        c = pyqrcode.create(add)
        c.png(f'{product_name}.png', scale=6)
        with open('/home/vasu/Vasu/freshersbatch4/project1/qr code.png', 'rb')as img:
            encoded = base64.b64encode(img.read())
            user = QR_Code.objects.create(product_name=product_name, product_code=product_code, pack_code=pack_code, qr_code=encoded)
            user.save()
            return user






