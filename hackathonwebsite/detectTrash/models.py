from django.db import models


class Locations(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    goal = models.IntegerField(default=10)