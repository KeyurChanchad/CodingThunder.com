from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
 
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, "login.html")

def userlogout(request):
    # logout(request)
    return redirect(request, 'logout.html')
