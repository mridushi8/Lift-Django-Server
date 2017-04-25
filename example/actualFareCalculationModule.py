from abc import ABCMeta, abstractmethod
import base64
import collections
import datetime
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from datetime import datetime, time as datetime_time, timedelta

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


@permission_classes((permissions.AllowAny,))
def getActFare(request):
    if request.method == "GET":
        distance = request.GET["distance"]
        startTime = request.GET["startTime"]
        endTime = datetime.datetime.now()

        a = actualFareCalculate()
        return HttpResponse(a.getActualFare(self, distance, startTime, endTime))

class actualFareCalculate():

    def getActualFare(self, distance, startTime, endTime):


        dist = distance
        sTime= startTime
        eTime= endTime

        def time_diff(start, end):
            if isinstance(start, datetime_time):  # convert to datetime
                assert isinstance(end, datetime_time)
                start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
            if start <= end:  # e.g., 10:33:26-11:15:49
                return end - start
            else:  # end < start e.g., 23:55:00-00:25:00
                end += timedelta(1)  # +day
                assert end > start
                return end - start
        time = time_diff(sTime,eTime)
        time_rate = 0.017
        distance_rate = 0.005
        base_fare = 20

        time_value = time_rate * time
        distace_value = distance_rate * dist
        actual_fare = base_fare + time_value + distace_value


        return actual_fare






