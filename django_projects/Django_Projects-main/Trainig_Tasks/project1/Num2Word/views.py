from .serializer import NumSerializer
from rest_framework import generics
from rest_framework.response import Response


class Register(generics.GenericAPIView):
    serializer_class = NumSerializer

    def post(self, request):
        num = NumSerializer(data=request.data)
        if num.is_valid(raise_exception=True):
            n = num.save()
            return Response(NumSerializer(n).data)



