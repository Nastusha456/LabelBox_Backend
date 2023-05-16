from django.urls import path

from lablebox.views import index

app_name="lablebox"

urlpatterns = [
    path("index/", index, name="index"),

]