from django.urls import path
from . import views

app_name = 'newsletter'
urlpatterns = [
    path('', views.GetRoutes.as_view(), name='get_routes'),
    path('subscribe/', views.Subscribe.as_view(), name='subscribe'),
    path('unsubscribe/', views.Unsubscribe.as_view(), name='unsubscribe'),
]