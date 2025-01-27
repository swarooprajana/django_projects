from django.shortcuts import render
from .models import Decimal
from .serializer import DecimalSerializer
from rest_framework import generics
from rest_framework.response import Response


class Register(generics.GenericAPIView):
    serializer_class = DecimalSerializer

    def post(self, request):
        d = DecimalSerializer(data=request.data)
        if d.is_valid(raise_exception=True):
           k = d.save()
           return Response(DecimalSerializer(k).data)
