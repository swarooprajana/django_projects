from django.shortcuts import render
from .models import DOB
from datetime import date
from datetime import datetime
from .serializer import DOBSerializer
from rest_framework.response import Response
from rest_framework import generics
import datetime


class Register(generics.GenericAPIView):
    serializer_class = DOBSerializer

    def post(self, request):
         today = date.today()
         print(type(today))
         year = today.year
         print(type(year))
         Age = request.data.get('Age')
         print(type(Age))
         dob = int(Age)-year
         return Response({"DOB": dob})

