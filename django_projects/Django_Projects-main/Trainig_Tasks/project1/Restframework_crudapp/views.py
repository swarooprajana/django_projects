from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Student
from rest_framework import generics


# # CREATE
#
# @api_view(['POST'])
# def Create(request):
#     x = Student.objects.all()
#     y = StudentSerializer(data=request.data)
#     if y.is_valid():
#         y.save()
#     return Response(y.data)
#
#
# # READ
#
# @api_view(['GET'])
# def Read(request):
#     x = Student.objects.all()
#     y = StudentSerializer(x, many=True)
#     return Response(y.data)
#
#
# # UPDATE
#
# @api_view(['POST'])
# def Update(request, id):
#     x = Student.objects.get(id=id)
#     y = StudentSerializer(x, data=request.data)
#     if y.is_valid():
#         y.save()
#     return Response(y.data)
#
#
# # DELETE
#
# @api_view(['DELETE'])
# def Delete(request, id):
#     x = Student.objects.get(id=id)
#     x.delete()
#     return Response("deleted")


# Generics

class create(generics.GenericAPIView):
    serializer_class = StudentSerializer
    permission_class = (IsAuthenicated)

    def post(self, request):
        a = StudentSerializer(data=request.data)
        if a.is_valid(raise_exception=True):
            u = a.save()
            return Response(StudentSerializer(u).data)


class read(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class update(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def put(self, request, id):
            r = Student.objects.get(id=id)
            # r.name = request.data.get('name')
            # r.age = request.data.get('age')
            # r.email = request.data.get('email')
            # r.address = request.data.get('address')
            # r.college = request.data.get('college')
            s = StudentSerializer(r, data=request.data)
            s.is_valid(raise_exception=True)
            s.save()
            return Response(s.data)


class delete(generics.DestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer


# generic direct method

'''class BookList(generics.ListCreateAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer


class BookDetails(generics.RetrieveUpdateAPIView):
      queryset = Student
      serializer_class = StudentSerializer

class BookDelete(generics.DestroyAPIView):
      queryset = Student
      serializer_class = StudentSerializer'''
