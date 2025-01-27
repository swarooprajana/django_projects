from django.shortcuts import render
from .models import *
from .Serializer import *
from rest_framework import generics
from rest_framework.response import Response




class create(generics.GenericAPIView):
      serializer_class = ORMSerializer

      def post(self,request):
         x = ORMSerializer(data=request.data)
         if x.is_valid (raise_exception=True):
             y = x.save()
             return Response(ORMSerializer(y).data)


class file(generics.GenericAPIView):
    serializer_class = OneToOneserializer

    def post(self,request):
        a = OneToOneserializer(data=request.data)
        if a.is_valid(raise_exception=True):
            b = a.save()
            return Response(OneToOneserializer(b).data)


class dairy(generics.GenericAPIView):
    serializer_class = OneToMany

    def post(self,request):
        c = OneToMany(data=request.data)
        if c.is_valid(raise_exception=True):
          d = c.save()
          return Response(OneToMany(d).data)

#
# class Getdetail(generics.GenericAPIView):
#     serializer_class = OneToOneserializer
#
#     def get(self, request, id):
#         customer_details = College.objects.filter(id=id)
#         print(customer_details)
#         serializer = OneToOneserializer(customer_details, many=True)
#         return Response(serializer.data)



class colllegeget(generics.GenericAPIView):
    serializer_class = OneToOneserializer
    def get(self,request,College):
        a=Room.objects.filter(College_id=College)
        user=OneToOneserializer(a,many=True)
        return Response(OneToOneserializer(user).data)




