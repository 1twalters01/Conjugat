from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'settings'
urlpatterns = [
    path('close-account/', views.close_account, name='close_account'),
    path('change-password/', views.change_password.as_view(), name='change_password'),
    path('change-password/done/', views.change_password_done.as_view(), name='change_password_done'),
    path('change-email/', views.change_email, name='change_email'),
    path('change-email/done/', views.change_email_done, name='change_email_done'),
    path('change-username/', views.change_username, name='change_username'),
    path('change-username/done/', views.change_username_done, name='change_username_done'),
    path('themes/', views.themes, name='themes'),
    path('premium/', views.premium, name='premium'),
    path('two-factor-auth/', views.two_factor_auth, name='two_factor_auth'),
    path('reset-account/', views.reset_account, name='reset_account'),
]