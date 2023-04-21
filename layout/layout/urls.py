"""layout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from lablebox.views import index
from vueapp.views import index
from classificator.views import UserObjectsView
from annotation.views import AnnotationObject


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls", namespace="users")),
    path('', index, name="index"),
    path('classificator/', include(("classificator.urls", "classificator"), namespace="classificator")),#ClassificatorAPIView.as_view())
    path('ann/', include(("annotation.urls", "annotation"), namespace="annotation"))
]

