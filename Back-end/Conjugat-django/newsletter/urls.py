from django.urls import path
from . import views
from . import webhooks

app_name = 'newsletter'
urlpatterns = [
    path('ping/', views.mailchimp_ping_view),
    path('subscribe', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]