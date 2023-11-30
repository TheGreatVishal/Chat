from django.urls import path
from . import views

urlpatterns = [
    path("chat", views.chat, name = "chat"),
    path("get_messages", views.get_messages, name = "get_messages"),
    path("get_messages_dm/<str:message_table>", views.get_messages_dm, name = "get_messages_dm"),
    path("put_message", views.put_message, name = "put_message"),
    path("put_messages_dm/<str:message_table>", views.put_messages_dm, name = "put_messages_dm"),
    path("reset_chat", views.reset_chat, name = "reset_chat"),
    path("reset_chat_dm/<str:message_table>/<str:name>", views.reset_chat_dm, name = "reset_chat_dm"),
    path("direct_chat", views.direct_chat, name = "direct_chat"),
    path("dm/<str:receiver>", views.dm, name = "dm"),
    
]