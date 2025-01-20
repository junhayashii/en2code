from django.urls import path
from .views import CourseDetailView

urlpatterns = [
    path('<str:course_id>/', CourseDetailView.as_view(), name='course_detail'),
]