from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    allposts = {'allposts' : posts}
    return render(request, 'blog/blog.html', allposts)

def blogpost(request, slug):    
    post = Post.objects.filter(slug=slug).first()  #  Post.objects.filter(slug=slug)[0]
    post.views= post.views +1
    post.save()

    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)

    replyDict = {}
    for reply in replies:
        if reply.parent.postSno not in replyDict.keys():
            replyDict[reply.parent.postSno] = [reply]
        else:
            replyDict[reply.parent.postSno].append(reply)
            
    context = {'post' : post, 'comments': comments, 'user': request.user, 'replyDict':replyDict}
    return render(request, 'blog/blogpost.html', context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        sno = request.POST.get("sno")
        post = Post.objects.get(sno=sno)   # Post.objects.filter(sno = [sno]) not work
        parentSno= request.POST.get('parentSno')
        
        if parentSno == "":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(postSno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")
    
        