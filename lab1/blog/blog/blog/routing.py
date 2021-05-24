from django.conf.urls import url
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path(r'articles/chats/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
