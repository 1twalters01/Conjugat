from django.urls import path
from . import views

app_name = 'verbs'
urlpatterns = [
    path('verb-test', views.verb_test, name='verb-test'),
]