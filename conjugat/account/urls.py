from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('login/username/', views.loginView, name='login'),
    path('login/password/', views.loginPasswordView, name='login_Password'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('activate/<uidb64>/<token>/', views.activateView, name='activate'),
    path('password-reset/', views.passwordResetView,name='password_reset'),

    # path('login/', views.user_login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', views.NewPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.NewPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('register/', views.register, name='register'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]