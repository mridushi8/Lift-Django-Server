from abc import ABCMeta, abstractmethod
import base64
import collections
import datetime
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from datetime import datetime, time as datetime_time, timedelta
from driver_request.models import Driver_Request
from passenger_requests.models import Trip_Request

import functools
import hashlib
import hmac
import re
import requests
import random
import time
import json
import googlemaps
from django.http import HttpResponse

from googlemaps import convert
from googlemaps.convert import as_list

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def getActFare(request):
    if request.method == "POST":
        distance = float(request.POST["distance"])
        startTime = request.POST["startTime"]
        Id = request.POST["driver_id"]
        endTime = datetime.now()
        startTimeConverted = datetime.strptime(startTime, '%b %d %Y %H:%M')

        a = actualFareCalculate()
        req = Trip_Request()
        req = Trip_Request.objects.filter(driver_id=Id).first()
        req.actual_fare = a.getActualFare(distance, startTimeConverted, endTime)
        req.save()
        print (req.actual_fare)

        return HttpResponse(a.getActualFare(distance, startTimeConverted, endTime))

class actualFareCalculate():

    def getActualFare(self, distance, startTime, endTime):
        dist = distance
        sTime= startTime
        eTime= endTime

        time = (eTime -sTime).total_seconds
        time_rate = 0.017
        distance_rate = 0.005
        base_fare = 20

        time = abs((endTime - startTime).total_seconds())
        time_value = time_rate * float(time)
        distace_value = distance_rate * dist
        actual_fare = base_fare + time_value + distace_value

        return str(actual_fare)

