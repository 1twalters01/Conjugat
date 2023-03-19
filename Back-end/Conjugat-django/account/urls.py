
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetRoutes.as_view(), name='get_routes'),

    path('login/username/', views.LoginUsername.as_view(), name='login_username'),
    path('login/password/', views.loginPasswordView, name='login_Password'),

    path('logout/', views.logoutView, name='logout'),
    
    path('register/', views.registerView, name='register'),
    path('activate/', views.Activate.as_view(), name='activate'),

    path('password-reset/', views.passwordResetView, name='password_reset'),
    path('password-reset/confirm', views.passwordResetConfirmView, name='password_reset_confirm'),
]