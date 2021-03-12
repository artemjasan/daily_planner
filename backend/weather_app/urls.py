from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListCity,DetailCity, CityWeather

urlpatterns = [
    path('', CityWeather.as_view()),
    path('city/', ListCity.as_view()),
    path('city/<int:pk>/', DetailCity.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
