import requests

from rest_framework import generics
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import City
from .serializer import CitySerializer

URL_API = "http://api.openweathermap.org/data/2.5/weather?q={}"
UNIT_SYSTEM = "units=metric"
API_ID = "appid=74fda670f4fb3091728731208163e6d8"
API_CALL = f"{URL_API}&{UNIT_SYSTEM}&{API_ID}"


def call_api(city_name):
    city_weather = requests.get(API_CALL.format(city_name)).json()
    if city_weather["cod"] == 200:
        weather_data = {
            "city": city_name,
            "temperature": city_weather["main"]["temp"],
            "description": city_weather["weather"][0]["description"],
            "icon": city_weather["weather"][0]["icon"]
        }
        return weather_data
    err_msg = {
        "message": f'City {city_name} does not exist in this world!'
    }
    return err_msg


class ListCity(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DetailCity(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityWeather(GenericAPIView):
    queryset = City.objects.values_list("name", flat=True)

    def get(self, request):
        cities = self.get_queryset()
        weather_data = []

        for city in cities:
            city_weather = call_api(city)
            weather_data.append(city_weather)

        return Response(weather_data)
