from django.urls import path
from .views import AnnotationObjectView

app_name = "annotation"
urlpatterns = [
    path('<int:user_id>/annotation/<int:pk>/', AnnotationObjectView.as_view())
]