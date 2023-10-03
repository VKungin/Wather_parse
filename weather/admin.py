from django.contrib import admin

from weather.models import Weather


class WeatherAdmin(admin.ModelAdmin):
    list_display = ("date", "temperature", "weather_description")


admin.site.register(Weather, WeatherAdmin)
