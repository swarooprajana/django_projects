import django as django
from django.shortcuts import render
from.models import logging
from.serializer import LoggingSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
import logging


# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


class log(generics.GenericAPIView):
    serializer_class = LoggingSerializer

    def post(self, request):
        l = LoggingSerializer(data=request.data)
        if l.is_valid(raise_exception=True):
           k = l.save()
           return Response((l).data)

