from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
 def create(self,validated_data):
  validated_data["password"] = make_password(validated_data["password"])
  return super(RegisterSerializer,self).create(validated_data)
 class Meta:
  model = User
  fields = "__all__"

class LoginSerializer(serializers.Serializer):
 username = serializers.CharField()
 password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = User
  fields = ["id","email","username","password"]
 def validate_password(self, value):
  return make_password(value)
 def create(self, validated_data):
  validated_data['password'] = self.validate_password(validated_data['password'])
  return super().create(validated_data)
 def update(self, instance, validated_data):
  return super().update(instance, validated_data)