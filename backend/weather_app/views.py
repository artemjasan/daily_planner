import requests

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City
from .serializer import CitySerializer


class WeatherList(APIView):
    URL_API = "http://api.openweathermap.org/data/2.5/weather?q={}"
    UNIT_SYSTEM = "units=metric"
    API_ID = "appid=74fda670f4fb3091728731208163e6d8"

    api_call = f"{URL_API}&{UNIT_SYSTEM}&{API_ID}"

    def get(self, request):
        cities = City.objects.all()
        serializator = CitySerializer(cities, many=True)
        weather_data = []

        for city in cities:
            req = requests.get(WeatherList.api_call.format(city)).json()

            city_weather = {
                "city": city.name,
                "temperature": req["main"]["temp"],
                "description": req["weather"][0]["description"],
                "icon": req["weather"][0]["icon"]
            }

            weather_data.append(city_weather)
        return Response(weather_data)
