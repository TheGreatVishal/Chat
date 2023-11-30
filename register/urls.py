from django.urls import path
import register.views as views

urlpatterns = [
    path("", views.welcome, name = "welcome"),
    path("signup", views.signup, name = "signup"),
    path("login", views.login, name = "login"),
    path("welcome", views.welcome, name = "welcome"),
    path("logout", views.logout, name = "logout"),
    path("developer_info", views.developer_info, name = "developer_info"),
]