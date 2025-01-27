from rest_framework import serializers
# from .models import User
from django.contrib.auth.hashers import make_password
#from django.db.models.query_utils import DeferredAttribute
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
            paa = validated_data['password']
            user = User.objects.create(username=validated_data['username'], password=make_password(paa),email=validated_data['email'])
            user.save()
            return user


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')



