import os
import requests

from dotenv import load_dotenv, find_dotenv
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import City
from .serializer import CitySerializer

#  load to the project sensitive dates
load_dotenv(find_dotenv())

URL_API = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric"
API_KEY = os.environ.get("API_KEY")
API_CALL_URL = f"{URL_API}&{API_KEY}"
MAX_AMOUNT = 3  # Max of cities in list


def parse_weather_data(response):
    weather_data = response.json()
    parsed_weather_data = {
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["description"],
        "icon": weather_data["weather"][0]["icon"]
    }
    return parsed_weather_data


def open_weather_api(city_name):
    data = None
    error_message = None

    response = requests.get(API_CALL_URL.format(city_name))
    if response.ok:
        data = parse_weather_data(response)
    else:
        error_message = f'City {city_name} does not exist in this world!'

    return {
        "city": city_name,
        "data": data,
        "error": error_message,
    }


class ListCity(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.count() >= MAX_AMOUNT:
            return Response("Maximum amount of cities", status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class DetailCity(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityWeather(GenericAPIView):
    queryset = City.objects.values_list("name", flat=True)

    def get(self, request):
        cities = self.get_queryset()
        weather_data = [open_weather_api(city) for city in cities]
        return Response(weather_data)
