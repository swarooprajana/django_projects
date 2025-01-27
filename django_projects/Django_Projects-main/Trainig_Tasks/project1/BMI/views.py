from django.shortcuts import render
from .serializer import BMISerializer
from rest_framework import generics
from rest_framework.response import Response


class Register(generics.GenericAPIView):
    serializer_class = BMISerializer

    def post(self, request):
        ser = BMISerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            b = ser.save()
            return Response(BMISerializer(b).data)
