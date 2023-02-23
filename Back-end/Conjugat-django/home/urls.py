from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
#     path('', views.landing_page, name='landing'),
#     path('contact',views.contact, name='contact'),
#     path('faq',views.faq, name='faq'),
#     path('privacy',views.privacy, name='privacy'),
#     path('terms', views.terms, name='terms'),
]