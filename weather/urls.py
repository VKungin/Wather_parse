from django.urls import path
from .views import WeatherData, WeatherList, WeatherDetail

urlpatterns = [
    path('weather_data/', WeatherData.as_view(), name='weather-data'),
    path('weather_list/', WeatherList.as_view(), name='weather-list'),
    path('<int:pk>/', WeatherDetail.as_view(), name='weather-detail'),
]
app_name = "weather"
