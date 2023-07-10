"""
ASGI config for conjugat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack #Change this to work for knox
import messagesFunctionality.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conjugat.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
           messagesFunctionality.routing.websocket_urlpatterns
        )
    )
})
