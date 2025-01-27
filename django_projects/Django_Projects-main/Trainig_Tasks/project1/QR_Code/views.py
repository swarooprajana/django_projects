from django.shortcuts import render
from .models import QR_Code
from .serializer import QRCodeSerializer
from rest_framework import generics
from rest_framework.response import Response


class Register(generics.GenericAPIView):
    serializer_class = QRCodeSerializer

    def post(self, request):
        q = QRCodeSerializer(data=request.data)
        if q.is_valid(raise_exception=True):
           k = q.save()
           return Response(QRCodeSerializer(k).data)


def get(request):
        products = QR_Code.objects.all()
        return render(request, "get.html", {"image": products})
