from django.urls import path
from . import views

app_name = 'verbs'
urlpatterns = [
    path('verb-random-retrieval', views.VerbRandomRetrieval.as_view(), name='verb-random'),
    path('verb-test', views.VerbTest.as_view(), name='verb-test'),
    path('verb-test-results', views.VerbTestResults.as_view(), name='verb-results'),
]
