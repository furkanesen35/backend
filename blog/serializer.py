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
 user = serializers.SerializerMethodField()
 class Meta:
  model = Comment
  fields = "__all__"
 def get_user(self, obj):
  if obj.user:
   return obj.user.username
  return None
 def validate(self, data):
  if not data.get("user"):
   raise serializers.ValidationError("A user must be associated with the comment.")
  if not data.get("post"):
   raise serializers.ValidationError("A post must be associated with the comment.")
  return data

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
#  def create(self, validated_data):
#   return super().create(validated_data)
#  def update(self, instance, validated_data):
#   return super().update(instance, validated_data)