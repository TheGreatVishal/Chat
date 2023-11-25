from django.urls import path
import register.views as views

urlpatterns = [
    path("", views.welcome, name = "welcome"),
    path("signup", views.signup, name = "signup"),
    path("login", views.login, name = "login"),
    path("welcome", views.welcome, name = "welcome"),
    # path("home", views.welcome, name = "home"),
]