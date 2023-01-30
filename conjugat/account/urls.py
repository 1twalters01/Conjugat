from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', views.NewPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.NewPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-resetcomplete//', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]