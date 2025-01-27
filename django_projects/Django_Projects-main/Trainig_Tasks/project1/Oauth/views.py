from django.shortcuts import render
from.models import *
from.serializer import *
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
#from django.db.models.query_utils import DeferredAttribute
from django.contrib.auth.models import User


class Registration(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        a = UserSerializer(data=request.data)
        a.is_valid(raise_exception=True)
        n = a.save()
        return Response({
            "user": UserSerializer(n, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(n)[1]
        })


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Login(request, user)
        return Response(LoginSerializer(user).data)






