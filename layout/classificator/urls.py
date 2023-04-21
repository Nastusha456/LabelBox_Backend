from django.urls import path
from .views import UserObjectsView

app_name = "classificator"
urlpatterns = [
    path('<int:user_id>/classifier/<int:pk>/', UserObjectsView.as_view())
]