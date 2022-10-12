from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.db.models import Max

# APIs Views 
def index(request):
    views =[]
    for post in Post.objects.all():
        views.append(post.views)
        
    def Max3Element(list1, N):
        max_list =[]
        for i in range(0, N):
            max1 = 0
            for j in range(len(list1)):	
                if list1[j] > max1:
                    max1 = list1[j]        
            list1.remove(max1);
            max_list.append(max1)
        return max_list
            
    max_list = Max3Element(views, 3)
    minimum = min(max_list)

    posts = Post.objects.filter(views__gte = minimum)
    allposts = {'allposts' : posts}
    return render(request, 'home/home.html', allposts)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        content = request.POST['content']

        if len(name) < 4  or len(email) < 10 or len(phone) < 9 or len(address) < 10:
            messages.error(request, 'Please fill the form correctly!')
        else:
            contact = Contact(name=name, email=email, phone=phone, address=address, content=content)
            contact.save()
            messages.success(request, 'Your message has been sent successfully.')

    return render(request, 'home/contact.html')

def search(request):   
    query = request.GET['search']

    if len(query) > 30:
        allPosts = Post.objects.none() 
    else:
        allPostsTitle  = Post.objects.filter(title__icontains = query)
        allPostsContent  = Post.objects.filter(content__icontains = query)
        allPostsAuthor  = Post.objects.filter(author__icontains = query)
        allPosts = allPostsTitle.union(allPostsAuthor, allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, 'No serch result found. Please refind your quary!')
        
    post = {'allposts' : allPosts, 'query': query}
    # print(post)
    return render(request, 'home/search.html', post)

# username = keyur123
# password = keyur@123

# APIs Views 
def handleSignUp(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, 'User name must be under 10 characters')
            return redirect('/')    

        if not username.isalnum():
            messages.error(request, 'User name should only contain letters and number.')
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, 'Passwords must match.')
            return redirect('/')

        if User.objects.filter(username__iexact = username).exists():
            messages.error(request,'Username already exists')
            return redirect('/')

        # Create the user
        user = User.objects.create(username=username, email=email, password=pass1)
        user.first_name= fname
        user.last_name= lname
        user.save()
        messages.success(request, 'Your iCoder account has been successfully created.')
        return redirect('/')

    return HttpResponse("404 - page not found")

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginname = request.POST['loginUsername']
        loginpass = request.POST['loginPassword']

        user = authenticate(username= loginname, password= loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

