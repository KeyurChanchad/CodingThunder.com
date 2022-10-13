from  home import views    
# from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),  
    path('about', views.about, name='aboout'),  
    path('services', views.services, name='services'),  
    path('contact', views.contact, name='contact'),  
]  

