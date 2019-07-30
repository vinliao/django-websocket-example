from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)

    # this is for checking whether the conncetion is websocket or normal https
    # if the connection is websocket, then it will be handled by AuthMiddlewareStack
    # else it will be handled normally

    # the URLRouter is used for mapping the url in the http call to the consumer
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})