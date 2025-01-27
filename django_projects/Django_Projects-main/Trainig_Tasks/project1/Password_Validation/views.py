from django.shortcuts import render
from .models import password_validation
from rest_framework.response import Response
from.serializer import ValidatorSerializer
from rest_framework import generics
from django.http import JsonResponse

class Reg(generics.GenericAPIView):
    serializer_class = ValidatorSerializer

    def post(self, request):
       v = ValidatorSerializer(data=request.data)
       if v.is_valid(raise_exception=True):
          p = v.save()
          return Response(ValidatorSerializer(p).data)

