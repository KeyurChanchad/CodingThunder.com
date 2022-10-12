from django.shortcuts import render
from . models import BlogPost

# Create your views here.
def index(request):
    myposts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'myposts' : myposts})

def blogpost(request, id):
    post = BlogPost.objects.filter(blogpost_id = id)[0]
    return render(request, 'blog/blogpost.html', {'post' : post})