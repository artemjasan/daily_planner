from django.urls import path

from .views import WeatherList

urlpatterns = [
    path('', WeatherList.as_view()),
]


