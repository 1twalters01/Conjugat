
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetRoutes.as_view(), name='get_routes'),

    # path('obtain-csrfToken/', views.GetCSRF.as_view(), name='obtain_csrfToken'),

    path('login/username/', views.LoginUsername.as_view(), name='login_username'),
    path('login/password/', views.LoginPassword.as_view(), name='login_Password'),

    path('logout/', views.Logout.as_view(), name='logout'),
    
    path('register/', views.Register.as_view(), name='register'),
    path('activate/', views.Activate.as_view(), name='activate'),

    path('password-reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password-reset/confirm', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
]