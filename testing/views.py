
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from testing.models import User
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def checkproof(request):
    if request.method == 'POST':
        Id = request.POST.get('id')
        checkuser = User.objects.get(id=Id)
        print checkuser.carno
        print checkuser.identity
        if checkuser.carno is not None and checkuser.identity!="":
		    return Response("1")
        else:
		    return Response("0")

		


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def checkmatch(request):
    if request.method == 'POST':
        id= request.POST.get('email')
        pwd= request.POST.get('pass')
        try:
            checkuser = User.objects.get(email=id)
        except ObjectDoesNotExist:
            checkuser = None
        print checkuser
        if checkuser is None:
            return Response("nouser")
			
        elif checkuser is not None:  		
            if pwd == checkuser.password:
                response_data = {}
                response_data['id'] = checkuser.id
                response_data['name'] = checkuser.name
                return Response(response_data)
            else:
                return Response("nomatch")
			

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Homeadd = request.POST.get('homeadd')
        Carno = request.POST.get('carno')
        Pw = request.POST.get('pass')
        user_obj = User()

        user_obj.name=Name
        user_obj.email=Email 
        user_obj.phone= Phone
        user_obj.home_add=Homeadd
        user_obj.carno= Carno
        user_obj.password=Pw
        user_obj.save(force_insert=True)
        return Response("success") 
        
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def picupload(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        print type
        image = request.POST.get('image')
        id= request.POST.get('id')
        try:
            checkuser = User.objects.get(id=id)
        except ObjectDoesNotExist:
            checkuser = None
        print checkuser
        if checkuser is None:
            return Response("nouser")
			
        elif checkuser is not None:  	
            if type == "iden": 
                checkuser.identity = image
                checkuser.save()
                return Response("doneiden")
                print checkuser.identity
            elif type == "driv":
                checkuser.pic = image
                checkuser.save()
                print checkuser.pic
                return Response("picuploaded")

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def forgetpass(request):
    if request.method == 'POST':
        id= request.POST.get('email')
        pwd= request.POST.get('pass')
        try:
            checkuser = User.objects.get(email=id)
        except ObjectDoesNotExist:
            checkuser = None
        print checkuser
        if checkuser is None:
            return Response("nouser")
			
        elif checkuser is not None:  		
            checkuser.password = pwd
            checkuser.save()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("liftcarapp@gmail.com", "liftcarapp1234")
            msg = "Your new pssword is "+pwd +"."
            server.sendmail("liftcarapp@gmail.com", id, msg)
            server.quit()
            return Response("done")
        
@api_view(['GET', 'POST'])       
@permission_classes((permissions.AllowAny,))
def getAvgRating(request):
    number = float(request.data['rating'])
    userid = int(request.data['userid'])
    rating_user = User()
    rating_user = User.objects.get(id=userid)

    if rating_user.number_of_ratings == None:
        rating_user.number_of_ratings = 0
    if rating_user.avg_rating == None:
        rating_user.avg_rating = "0"

    avg_rating = float(rating_user.avg_rating)

    rating_user.number_of_ratings = rating_user.number_of_ratings + 1
    avg_rating = (avg_rating * (rating_user.number_of_ratings-1) + number)/ rating_user.number_of_ratings
    rating_user.avg_rating = str(avg_rating)
    rating_user.save()
    print rating_user.avg_rating
    return HttpResponse("")

def get_user(request):
    Id = request.data['id']
    req = Trip_Request.objects.get(id=Id)
    return HttpResponse(json.dumps(req.as_json()), content_type="application/json")

	
