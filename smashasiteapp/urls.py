from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('music.html', views.about, name="music"),
    path('contact.html', views.contact, name="contact")
]