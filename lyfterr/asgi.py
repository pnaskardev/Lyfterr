"""
ASGI config for lyfterr project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from trips.consumers import TaxiConsumer
from .middleware import TokenAuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lyfterr.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('taxi/', TaxiConsumer.as_asgi())
        ])
    )
})
