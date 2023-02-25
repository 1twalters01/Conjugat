from django.urls import path
from . import views

app_name = 'newsletter'
urlpatterns = [
    path('ping/', views.mailchimp_ping_view),
    path('subscribe/', views.subscribeView, name='subscribe'),
    path('subscribe/', views.unsubscribeView, name='subscribe'),

    # path('subscribe/', views.subscribe, name='subscribe'),
    # path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]