import generics as generics
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from .serializer import RegisterSerializer, LoginSerializer
from.models import Encrypt
from cryptography.fernet import Fernet



def  encrypt_password(password):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        password = fernet.encrypt(password.encode())
        return password


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        e = RegisterSerializer(data=request.data)
        e.username = request.POST.get("username")
        password = request.POST.get("password")
        e.name = request.POST.get("name")
        e.email = request.POST.get("email")
        e.Roll_No = request.POST.get("Roll_No")
        e.password = encrypt_password(password)
        if e.is_valid(raise_exception=True):
           e.save(password=encrypt_password(password))
           return Response(RegisterSerializer(e).data)



class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        ency = Encrypt.objects.get(username=username)
        print(username)
        if ency.password == encrypt_password(password):
            return HttpResponse("success")
        else:
            return HttpResponse("fail")

