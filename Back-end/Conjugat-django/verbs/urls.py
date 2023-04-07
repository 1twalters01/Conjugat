from django.urls import path
from . import views

app_name = 'verbs'
urlpatterns = [
    path('verb-test', views.VerbTest.as_view(), name='verb-test'),
]