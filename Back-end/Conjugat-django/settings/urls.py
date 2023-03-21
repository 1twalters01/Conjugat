from django.urls import path
from . import views

app_name = 'settings'
urlpatterns = [
    path('', views.GetRoutes.as_view(), name='getRoutes'),

    path('change-email/', views.ChangeEmail.as_view(), name='change_email'),
    path('change-password/', views.ChangePassword.as_view(), name='change_password'),
    path('change-username/', views.ChangeUsername.as_view(), name='change_username'),

    path('reset-account/', views.resetAccountView, name='reset_account'),
    path('close-account/', views.CloseAccount.as_view(), name='close_account'),

    path('premium/', views.premiumView, name='premium'),

    path('themes/', views.ChangeTheme.as_view(), name='themes'),
    path('two-factor-auth/', views.TwoFactorAuthentication.as_view(), name='two_factor_auth'),
]