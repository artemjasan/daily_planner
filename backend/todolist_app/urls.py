from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListTask, DetailTask, CategoriesList, PriorityList

urlpatterns = [
    path('', ListTask.as_view()),
    path('<int:pk>/', DetailTask.as_view()),
    path('languages/', CategoriesList.as_view(), name="list_categories"),
    path('priority/', PriorityList.as_view(), name="list_priority")
]

urlpatterns = format_suffix_patterns(urlpatterns)
