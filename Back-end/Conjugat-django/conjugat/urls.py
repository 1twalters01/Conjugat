"""conjugat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/login/', include('rest_social_auth.urls_knox')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('home.urls')),
    path('subscriptions/', include('subscription.urls')),
    path('verbs/', include('verbs.urls')),
    path('settings/', include('settings.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('newsletter/', include('newsletter.urls')),
]
