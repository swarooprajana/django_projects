from django.http import HttpResponse
from django.shortcuts import render
from.models import UserRegistration
from.serializer import RegistrationSerializer, loginSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view



class Registration(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        r = RegistrationSerializer(data=request.data)
        if r.is_valid(raise_exception=True):
            u = r.save()
            return Response(RegistrationSerializer(u).data)


class Login(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        page = UserRegistration.objects.get(username=username)
        print(username)
        if page.password == password:
           return HttpResponse('success')
        else:
            return HttpResponse('fail')


