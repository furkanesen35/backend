from django.shortcuts import get_object_or_404
from .models import Post, Comment, Category, Like, PostView
from django.contrib.auth.models import User
from .serializer import PostSerializer, CategorySerializer, CommentSerializer, LikeSerializer, ViewSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_all_post(request):
 posts = Post.objects.all()
 serializer = PostSerializer(posts, many=True)
 return Response(serializer.data)

@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_new_post(request):
 user = request.user
 request.data._mutable = True  # Optional for modifying `request.data`
 request.data["author"] = str(user.id)
 serializer = PostSerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
  return Response({"message": "Post created successfully"}, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def post_detail(request, slug):
 post = get_object_or_404(Post, slug=slug)
 serializer = PostSerializer(post)
 return Response(serializer.data, status=status.HTTP_200_OK)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["PUT"])
@parser_classes([MultiPartParser, FormParser])
def post_edit(request, slug):
 post = get_object_or_404(Post, slug=slug)
 data = request.data.copy()
 serializer = PostSerializer(post, data=data, partial=True)
 if serializer.is_valid():
  serializer.save()
  return Response({"message": "Post updated successfully"})
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
def post_delete(request, slug):
 post = get_object_or_404(Post, slug=slug)
 post.delete()
 return Response({"message": "Post deleted successfully"})

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_comments(request):
 comments = Comment.objects.all()
 serializer = CommentSerializer(comments, many=True)
 return Response(serializer.data)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def add_comment(request, slug):
 data = request.data.copy()  # Create a mutable copy
 user = User.objects.get(id=request.user.id)
 userid = str(user.id)
 post_id = str(get_object_or_404(Post, slug=slug).id)
 data["post"] = post_id
 data["user"] = userid
 serializer = CommentSerializer(data=data)
 if serializer.is_valid():
  serializer.save()
  return Response({"message": "Comment created successfully"}, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_category(request):
 categories = Category.objects.all()
 serializer = CategorySerializer(categories, many=True)
 return Response(serializer.data)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def add_category(request):
 serializer = CategorySerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
  return Response({"message": "Category created successfully"}, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def get_likes(request):
 likes = Like.objects.all()
 serializer = LikeSerializer(likes, many=True)
 return Response(serializer.data)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["POST"])
def toggleLike(request, slug):
 data = request.data.copy()  # Create a mutable copy
 user = User.objects.get(id=request.user.id)
 post = get_object_or_404(Post, slug=slug)
 data["user"] = user.id
 data["post"] = post.id
 like = Like.objects.filter(user=user.id, post=post.id)
 if like.exists():
  like.delete()
  return Response({"message": "Like deleted"})
 else:
  serializer = LikeSerializer(data=data)
  if serializer.is_valid():
   serializer.save()
   return Response({"message": "Like created", "data": serializer.data})
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_views(request):
 views = PostView.objects.all()
 serializer = LikeSerializer(views, many=True)
 return Response(serializer.data)

@api_view(["POST"])
def post_blog_view(request, slug):
 data = request.data.copy()  # Create a mutable copy
 post = get_object_or_404(Post, slug=slug)
 user = User.objects.get(id=request.user.id)
 data["post"] = post.id
 data["user"] = user.id
 serializer = ViewSerializer(data=data)
 if serializer.is_valid():
  serializer.save()
  return Response({"message": "View created successfully"}, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
