
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("register", views.register, name="register" ),
    path("login", views.login, name="login"),
    path("logout", views.logout_user, name="logout"),
    #CRUD
    path("dashboard", views.dashboard, name="dashboard"),
    path("create-record", views.create_record, name="create-record"),
    path('update-record/<int:id>/', views.update_record, name="update-record"),
    path('record/<int:id>/', views.view_record, name="record"),
    path('delete-record/<int:id>', views.delete_record, name="delete-record"),
]
  