from django.urls import path
from . import views

urlpatterns = [
    path("friend", views.friend, name = "friend"),
    path("requests", views.requests, name = "requests"),
    path("add_friend", views.add_friend, name = "add_friend"),
    path("send_request", views.send_request, name = "send_request"),
    path("accept/<str:source_user>", views.accept, name = "accept"),
    path("reject/<str:source_user>", views.reject, name = "reject"),    
    path("remove/<str:target>", views.remove, name = "remove"),
     path("get_users", views.get_users, name = "get_users"),
]