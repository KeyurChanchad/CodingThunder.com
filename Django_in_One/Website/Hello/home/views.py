from django.shortcuts import render  # For render templates
from django.http import HttpResponse
from home.models import Contact         #For database model
from datetime import datetime
from django.contrib import messages    #For message alert


# Create your views here.
def index(request):
    context={
        'name':'Keyur Chanchad',
        'age':'21'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Keyur bhai ho gay run ./index url run")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("/servieces is run")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("/about is run")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name=name, address=address, city=city, email=email, desc=desc, date = date)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
    return render(request, 'contact.html')
    # return HttpResponse("/Contact is run")







