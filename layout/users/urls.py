from django.urls import path
from users.views import Login, register, change

app_name="users"

urlpatterns = [
    path("login", Login, name="login"),
    path("register", register, name = "register"),
    path("change", change, name = "change"),
]
