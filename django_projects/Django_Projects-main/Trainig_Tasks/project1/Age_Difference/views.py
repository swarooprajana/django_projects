from django.shortcuts import render
from .models import Age_difference
from .serializer import DiffernceSerializer
from rest_framework.response import Response
from rest_framework import generics
from datetime import date
from datetime import datetime



class Register(generics.GenericAPIView):
    serializer_class = DiffernceSerializer

    def post(self, request):
        today = date.today()
        dob1 = request.data.get("dob1")
        dob2 = request.data.get("dob2")
        age = request.data.get("age")
        dob3 = datetime.strptime(str(dob1), "%Y-%m-%d").date()
        dob4 = datetime.strptime(str(dob2), "%Y-%m-%d").date()
        age = dob4.year - dob3.year
        ser = DiffernceSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
        return Response(({"result": age}))






