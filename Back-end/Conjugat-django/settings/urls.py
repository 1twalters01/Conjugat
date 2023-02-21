from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'settings'
urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),

    path('change-email/', views.changeEmailView, name='change_email'),
    path('change-password/', views.changePasswordView, name='change_password'),
    path('change-username/', views.changeUsernameView, name='change_username'),



    path('themes/', views.themesView, name='themes'),

    
    path('close-account/', views.close_account, name='close_account'),
    path('premium/', views.premium, name='premium'),
    path('reset-account/', views.reset_account, name='reset_account'),
    # path('themes/', views.themes, name='themes'),
    path('two-factor-auth/', views.two_factor_auth, name='two_factor_auth'),
]