from django.db import models


class Weather(models.Model):
    date = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    weather_description = models.TextField()

    def __str__(self):
        return self.date
