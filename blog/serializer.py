from rest_framework import serializers
from .models import Post,PostView,Category,Like,Comment

class CategorySerializer(serializers.ModelSerializer):
 class Meta:
  model = Category
  fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
 class Meta:
  model = Like
  fields = ('id', 'user', 'post')

class CommentSerializer(serializers.ModelSerializer):
 user = serializers.StringRelatedField()
 class Meta:
  model = Comment
  fields = "__all__"

class ViewSerializer(serializers.ModelSerializer):
 class Meta:
  model = PostView
  fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
 comments = CommentSerializer(many=True, read_only=True)
 likes = LikeSerializer(many=True, read_only=True)
 class Meta:
  model = Post
  fields = "__all__"