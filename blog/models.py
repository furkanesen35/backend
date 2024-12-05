from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
 return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
 name = models.CharField(max_length=100)
 class Meta:
  verbose_name_plural = "Categories"
 def __str__(self):
  return self.name

class Post(models.Model):
 OPTIONS = (
  ('d','Draft'),
  ('p','Published'),
 )
 title = models.CharField(max_length=100)
 content = models.TextField()
 image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
 category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
 publish_date = models.DateTimeField(auto_now_add=True)
 update_date = models.DateTimeField(auto_now=True)
 author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
 status = models.CharField(max_length=10, choices=OPTIONS, default='d')
 slug = models.SlugField(blank=True)
 def __str__(self):
  return self.title
 def comment_count(self):
  return self.comment_set.all().count()
 def view_count(self):
  return self.postview_set.all().count()
 def like_count(self):
  return self.like_set.all().count()
 def comments(self):
  return self.comment_set.all()
 
class Comment(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
 post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
 content = models.TextField()
 time_stamp = models.DateTimeField(auto_now_add=True)
 def __str__(self):
  return self.user.username
 
class Like(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
 def __str__(self):
  return self.user.username
 
class PostView(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 post = models.ForeignKey(Post, on_delete=models.CASCADE)
 time_stamp = models.DateTimeField(auto_now_add=True)
 def __str__(self):
  return self.user.username