from django.urls import path
from .consumer import ConsumerWebsocket

websocket_urlpatterns = [
    path('ws/save/<str:id_save>/', ConsumerWebsocket.as_asgi()),
]