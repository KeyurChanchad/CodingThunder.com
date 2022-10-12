from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about', views.about, name="About"),
    path('contact', views.contact, name="Contact"),
    path('tracker',views.tracker, name="TrackerStatus"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('search', views.search, name="Search"),
    path('checkout', views.checkout, name="Checkout"),
    path('handlerequest', views.handlerequest, name="HandleRequest"),
]
