
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("register", views.register, name="register" ),
    path("login", views.login, name="login"),
    path("dashboard", views.dashbaord, name="dashbaord"),
    path("logout", views.logout_user, name="logout")
]
  