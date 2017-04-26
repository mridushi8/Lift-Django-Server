from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Driver_Request(models.Model):
    request_id = models.IntegerField(primary_key=True)
    source_lat = models.CharField(max_length=200)
    source_long = models.CharField(max_length=200)
    destination_lat = models.CharField(max_length=200)
    destination_long = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=200)
    player_id = models.CharField(null=True,max_length = 500)
    actual_fare = models.CharField(max_length=10, null=True)

    def as_json(self):
        return dict(
            request_id=self.request_id,
            source_lat=self.source_lat,
            source_long=self.source_long,
            destination_lat=self.destination_lat,
            destination_long = self.destination_long,
            timestamp = self.timestamp,
            actual_fare = self.actual_fare)
