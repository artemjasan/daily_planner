from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListTask, DetailTask

urlpatterns = [
    path('', ListTask.as_view()),
    path('<int:pk>/', DetailTask.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
