from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import WeatherList, WeatherDetail

urlpatterns = [
    path('', WeatherList.as_view()),
    path('<int:pk>/', WeatherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
