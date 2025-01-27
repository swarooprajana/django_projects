from rest_framework import serializers
from .models import *



class ORMSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'



class OneToOneserializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["College","Total_Rooms","Persons"]



class OneToMany(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# class collegeserializer(serializers.ModelSerializer):
#     class Meta:
#         model = College
#         fields = "__all__"