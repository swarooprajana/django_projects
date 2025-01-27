from django.shortcuts import render
from .models import BarCode
from .serializer import BarCodeSerializer
from rest_framework import generics
from rest_framework.response import Response


class Register(generics.GenericAPIView):
    serializer_class = BarCodeSerializer

    def post(self, request):
        b = BarCodeSerializer(data=request.data)
        b.is_valid(raise_exception=True)
        user = b.save()
        return Response(BarCodeSerializer(user).data)
