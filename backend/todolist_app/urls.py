from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListTask, DetailTask, CategoriesList, PrioritiesList

urlpatterns = [
    path('', ListTask.as_view()),
    path('<int:pk>/', DetailTask.as_view()),
    path('categories/', CategoriesList.as_view(), name="list_categories"),
    path('priorities/', PrioritiesList.as_view(), name="list_priorities")
]

urlpatterns = format_suffix_patterns(urlpatterns)
