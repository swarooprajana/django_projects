from django.shortcuts import render
from .serializer import PasswordSerializer, UpdateSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.response import Response
from .models import ForgetModels
from django.http import HttpResponse


class Register(generics.GenericAPIView):
    serializer_class = PasswordSerializer

    def post(self, request):
        reg = PasswordSerializer(data=request.data)
        if reg.is_valid(raise_exception=True):
            var = reg.save()
            return Response(PasswordSerializer(var).data)


class update(generics.GenericAPIView):
    serializer_class = UpdateSerializer

    def put(self, request, id):
        data = ForgetModels.objects.get(id=id)
        data.password = request.data.get('password')
        data.save()
        return Response("success")


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        k = request.data.get('username')
        print(k)
        p = request.data.get("password")
        b = ForgetModels.objects.get(username=k)
        print(b.password)
        if b.password == p:
            return Response(LoginSerializer(b).data)
        else:
            return HttpResponse("invalid details")

