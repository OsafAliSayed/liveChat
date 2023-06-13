import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import group.routing
import group.consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moksh.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
                group.routing.websocket_urlpatterns
        )
    )
})
