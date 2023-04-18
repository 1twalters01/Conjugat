from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homeView.as_view(), name='home'),
    path('token-validator', views.authTokenValidator.as_view(), name='auth_token_validator')
]