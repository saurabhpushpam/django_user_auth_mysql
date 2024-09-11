from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields= ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model= User
    fields= ('username', 'email', 'password')

  def create(self, validated_data):
    user= User.objects.create_user(
      validated_data['username'],
      validated_data['email'],
      validated_data['password'],
    )
    return user
  

class loginSerializer(serializers.Serializer):
  username= serializers.CharField(required= True)
  password= serializers.CharField(required= True, write_only= True)