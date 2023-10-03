from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Weather
from .serializers import WeatherSerializer
from .parse import parse_days


class WeatherData(APIView):
    def post(self, request, format=None):
        weather_date = parse_days()
        data_to_save = []
        for date in weather_date:
            serializer = WeatherSerializer(data=date.__dict__)

            if serializer.is_valid():
                data_to_save.append(serializer.validated_data)

        Weather.objects.bulk_create([Weather(**data) for data in data_to_save])
        saved_data = [data for data in data_to_save]

        return Response(saved_data, status=status.HTTP_201_CREATED)


class WeatherList(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class WeatherDetail(generics.RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    lookup_field = 'pk'
