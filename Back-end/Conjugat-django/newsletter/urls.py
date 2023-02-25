from django.urls import path
from . import views

app_name = 'newsletter'
urlpatterns = [
    path('ping/', views.mailchimp_ping_view),
    path('subscribe/', views.subscribeView, name='subscribe'),
    path('unsubscribe/', views.unsubscribeView, name='subscribe'),
]