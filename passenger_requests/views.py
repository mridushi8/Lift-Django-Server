import json
from driver_matching import driver_matching
from passenger_requests.models import Trip_Request
from testing.serializers import UserSerializer
from testing.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def passenger_request(request):
    request_id = request.data['id']
    try:
        req = User.objects.get(id=request_id)
    except:
        return HttpResponse("User not found")

    newRequest = Trip_Request()
    newRequest.request_id = request_id
    newRequest.status = "101"
    newRequest.driver_id = "NULL"
    newRequest.source_lat = request.data['slat1']
    newRequest.source_long = request.data['slong1']
    newRequest.destination_lat = request.data['dlat1']
    newRequest.destination_long = request.data['dlong1']
    newRequest.timestamp = request.data['ts']
    newRequest.name = req.name
    newRequest.phone_no = req.phone
    newRequest.save()
    string = driver_matching(request_id)
    return HttpResponse(string)




@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_passenger(request):
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id=Id)
    return HttpResponse(json.dumps(req.as_json()), content_type="application/json")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_status(request): #Function to return status of request, polled continously by passenger's app
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id = Id)
    return HttpResponse(json.dumps(req.as_json()), content_type="application/json")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_driver(request): #Function to return driver id is called when status=303 ie driver is found
    Id = request.data['id']
    passenger = Trip_Request.objects.get(request_id = Id)
    driver_id = passenger.driver_id
    driver = User.objects.get(id = driver_id)
    return HttpResponse(json.dumps(driver.as_json()), content_type="application/json")


    
    
   


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def driver_response(request):
    passenger_id = request.data['request_id']
    req = Trip_Request.objects.get(request_id = passenger_id)
    req.driver_id = request.data['id']
 #   req.driver_lat = request.data['lat']
#    req.driver_long = request.data['long']
    req.status = "202"
    req.save()
    return HttpResponse("Done")


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def accept_driver(request):
    passenger_id = request.data['request_id']
    flag = request.data['flag']
    req = Trip_Request.objects.get(request_id = passenger_id)
    if(flag=="1"):
        req.driver_accept = 1
        req.status = "404"
        req.save()
    else:
        req.driver_accept = -1
        req.save()

    return HttpResponse("Done")

def check_flag(request):
    passenger_id = request.data['id']
    req = Trip_Request.objects.get(request_id = passenger_id)
    return HttpResponse(json.dumps(req.as_json()), content_type="application/json")


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def check_payment(request):
    passenger_id = request.data['id']
    req = Trip_Request.objects.get(request_id = passenger_id)
    if (req.payment_done == True):
        Driver_Request.objects.get(request_id=req.driver_id).delete()
        req.delete()
        return HttpResponse("True")
    else:
        return HttpResponse("False")









