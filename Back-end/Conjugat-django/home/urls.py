from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homeView.as_view(), name='home')
]