from .models import stamp_models
from .serializer import StampSerializer
from rest_framework.response import Response
from rest_framework import generics


class Register(generics.GenericAPIView):
    serializer_class = StampSerializer

    def post(self, request):
        ser = StampSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            k = ser.save()
            return Response(StampSerializer(k).data)


