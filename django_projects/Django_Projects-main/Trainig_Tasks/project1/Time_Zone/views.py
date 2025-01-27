from django.shortcuts import render
from .models import timezone
from .serializer import TimeSerializer
from rest_framework.response import Response
from rest_framework import generics


class Register(generics.GenericAPIView):
    serializer_class = TimeSerializer

    def post(self, request):
        var = TimeSerializer(data=request.data)
        if var.is_valid(raise_exception=True):
            t = var.save()
            return Response(TimeSerializer(t).data)
