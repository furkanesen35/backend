from django.urls import path
from .views import (
 get_all_post,
 add_new_post,
 post_detail,
 post_edit,
 get_category,
 get_comments,
 post_delete,
 add_comment,
 add_category,
 get_likes,
 get_views,
 post_blog_view,
 toggleLike
)

urlpatterns = [
 path('post/get/', get_all_post, name="get"),
 path('post/add/', add_new_post, name="add"),
 path('<str:slug>/post_edit', post_edit, name="post_edit"),
 path('<str:slug>/post_delete', post_delete, name="post_delete"),
 path('<str:slug>/post_detail', post_detail, name="post_detail"),
 path('comments/', get_comments, name="comments"),
 path('<str:slug>/post_comment', add_comment, name="post_comment"),
 path('get_category/', get_category, name="get_category"),
 path('add_category/', add_category, name="add_category"),
 path('get_likes/', get_likes, name="get_likes"),
 path('<str:slug>/post_like/', toggleLike, name="post_like"),
 path('get_views/', get_views, name="get_views"),
 path('<str:slug>/post_blog_view/', post_blog_view, name="post_blog_view"),
]