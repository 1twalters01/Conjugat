
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),

    path('login/username/', views.loginUsernameView, name='login'),
    path('login/password/', views.loginPasswordView, name='login_Password'),
    path('logout/', views.logoutView, name='logout'),
    
    path('register/', views.registerView, name='register'),
    path('activate/<uidb64>/<token>/', views.activateView, name='activate'),

    path('password-reset/', views.passwordResetView, name='password_reset'),
    path('password-reset/<uidb64>/<token>/', views.passwordResetConfirmView, name='password_reset_confirm'),
]