from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homeView.as_view(), name='home'),
    path('home/modal-data', views.homeModalView.as_view(), name='home_modal'),
    path('token-validator', views.authTokenValidator.as_view(), name='auth_token_validator')
]