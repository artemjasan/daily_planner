import requests
from django.http import Http404

from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City
from .serializer import CitySerializer

URL_API = "http://api.openweathermap.org/data/2.5/weather?q={}"
UNIT_SYSTEM = "units=metric"
API_ID = "appid=74fda670f4fb3091728731208163e6d8"

api_call = f"{URL_API}&{UNIT_SYSTEM}&{API_ID}"


class CitiesList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

"""
class WeatherList(APIView):
    def get(self, request, format=None):
        cities = City.objects.all()
        serializator = CitySerializer(cities, many=True)
        weather_data = []

        for city in cities:
            req = requests.get(api_call.format(city)).json()

            city_weather = {
                "id": city.id,
                "city": city.name,
                "temperature": req["main"]["temp"],
                "description": req["weather"][0]["description"],
                "icon": req["weather"][0]["icon"]
            }

            weather_data.append(city_weather)
        return Response(weather_data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherDetail(APIView):
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        weather_data = []
        city = self.get_object(pk)
        req = requests.get(api_call.format(city)).json()
        city_weather = {
            "id": city.id,
            "city": city.name,
            "temperature": req["main"]["temp"],
            "description": req["weather"][0]["description"],
            "icon": req["weather"][0]["icon"]
        }
        weather_data.append(city_weather)
        #serializer = CitySerializer(city)
        #return Response(serializer.data)
        return Response(weather_data)

    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""