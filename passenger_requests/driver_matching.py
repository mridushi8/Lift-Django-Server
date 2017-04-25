from driver_request.models import Driver_Request
from testing.models import User
from passenger_requests.models import Trip_Request
from geopy.distance import vincenty
from driver import send_pushnotif
import simplejson, urllib
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def distance_time(orig_coord,dest_coord):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&key=AIzaSyB8VxX2MRmHYTnv7QRrBSI3J7TIGILheQM".format(str(orig_coord),str(dest_coord))
    result= simplejson.load(urllib.urlopen(url))
    time = (result['rows'][0]['elements'][0]['duration']['value'])/60
    distance = (result['rows'][0]['elements'][0]['distance']['value'])/1000
    return (distance, time)



def filter( passenger_source, passenger_destination,driver_source,driver_destination):
    driver_distance, driver_time = distance_time(driver_source, driver_destination)
    d1,t1 = distance_time(driver_source,passenger_source)
    d2,t2 = distance_time(passenger_source,passenger_destination)
    d3,t3= distance_time(passenger_destination,driver_destination)
    driver_passenger_distance = d1+d2+d3
    driver_passenger_time = t1 + t2 +t3
    d= driver_passenger_distance-driver_distance
    t = driver_passenger_time - driver_time
    if ((d < 6) and (t<40)):
        print ("Filtered")
        return ("TRUE")
    else:
        print ("Not filtered")
        return ("FALSE")


def driver_matching(passenger_id):
    req = Trip_Request.objects.get(request_id=passenger_id)
    passenger_source = req.source_lat + "," + req.source_long
    passenger_destination = req.destination_lat + "," + req.destination_long

    driver_list = []
    not_empty = 0

    for driver in Driver_Request.objects.all():
        driver_source = driver.source_lat + "," + driver.source_long
        driver_destination = driver.destination_lat + "," + driver.destination_long
        if (filter(passenger_source, passenger_destination, driver_source, driver_destination) == "TRUE"):
            driver_list.append(driver.player_id)
            not_empty = 1

    if (not_empty == 0):
        req.status = 303
        req.save()
        return ("No Drivers Found")

    send_pushnotif(driver_list, passenger_id)
    return ("Notifications sent")










