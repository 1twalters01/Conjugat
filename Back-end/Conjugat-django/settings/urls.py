from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'settings'
urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),

    path('change-email/', views.changeEmailView, name='change_email'),
    path('change-password/', views.changePasswordView, name='change_password'),
    path('change-username/', views.changeUsernameView, name='change_username'),

    path('reset-account/', views.resetAccountView, name='reset_account'),
    path('close-account/', views.closeAccountView, name='close_account'),

    path('premium/', views.premiumView, name='premium'),

    path('themes/', views.themesView, name='themes'),
    path('two-factor-auth/', views.twoFactorAuthView, name='two_factor_auth'),
]