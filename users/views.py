from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["GET"])
def all_users(request):
 users = User.objects.all()
 serializer = RegisterSerializer(users, many=True)
 return Response(serializer.data)

@api_view(["POST"])
def register(request):
 serializer = RegisterSerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
  data = { "message" : f"Student {serializer.validated_data.get("username")} saved successfully!"}
  return Response(data, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_user_profile(request,id):
 user = get_object_or_404(User, id=id)
 serializer = UserSerializer(user)
 return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def ChangeUserInfoAndPassword(request, id):
 user = get_object_or_404(User, id=id)
 serializer = UserSerializer(user, data=request.data, partial=True)
 if serializer.is_valid():
  serializer.save()
  return Response({'message': 'User information updated successfully'})
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(TokenObtainPairView):
 def post(self, request, *args, **kwargs):
  response = super().post(request, *args, **kwargs)
  serializer = LoginSerializer(data=request.data)
  if serializer.is_valid():
   username = serializer.validated_data.get('username')
   password = serializer.validated_data.get('password')
   user = authenticate(request, username=username, password=password)
   if user is not None:
    login(request, user)
    token = response.data["access"]
    return Response({'message': 'Login successful', "TOKEN": token.key})
   response.set_cookie("access_token", token, httponly=True)
  return response
 
@api_view(['POST'])
def logout(request):
 try:
  refresh_token = request.COOKIES.get('refresh_token')
  if refresh_token is not None:
   token = RefreshToken(refresh_token)
   token.blacklist()
   return Response({'message': 'Logout successful'})
  else:
   return Response({'message': 'User not logged in'})
 except Exception as e:
  return Response({'message': 'Error logging out'}, status=500)