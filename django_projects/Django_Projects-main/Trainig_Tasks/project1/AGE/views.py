from django.shortcuts import render
from .models import Age
from .serializer import AgeSerializer
from rest_framework import generics
from datetime import datetime
from datetime import date
from rest_framework.response import Response


class Register(generics.GenericAPIView):
     serializer_class = AgeSerializer

     def post(self, request):
       today = date.today()
       dob = request.data.get("date")
       dob = datetime.strptime(str(dob), "%Y-%m-%d").date()
       age = today.year-dob.year
       return Response(({"AGE": age}))





