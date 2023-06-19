from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from trips.consumers import TaxiConsumer
from lyfterr.middleware import TokenAuthMiddlewareStack


application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddlewareStack(
        URLRouter([
            path('taxi/', TaxiConsumer.as_asgi())
        ])
    )
})
# application = ProtocolTypeRouter({
#     'websocket': URLRouter([
#         path('taxi/', TaxiConsumer)
#     ])
# })
