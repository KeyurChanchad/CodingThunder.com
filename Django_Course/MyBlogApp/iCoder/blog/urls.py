from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('postComment', views.postComment, name="postComment"), #1. /blog/postComment

    path('', views.blog, name='BlogHome'),  #/blog
    path('<str:slug>', views.blogpost, name='BlogPost'),  #2. /blog/string  A string given as slug 
]

#1 and 3 same so postcomment consider first