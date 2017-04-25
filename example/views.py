from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from example.models import TestClass
from example.serializers import TestClassSerializer
from django.db.models import Max
from django.shortcuts import render

class ListCreateTestClass(generics.ListCreateAPIView):
	queryset = TestClass.objects.all()
	serializer_class = TestClassSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def getMaxValue(request):
	print request.data
	number = request.data['num']
	print number
	queryset = TestClass.objects.all()
	newRecord = TestClass()
	newRecord.num = number
	newRecord.save()
	pr=queryset.aggregate(Max('num'))
	return Response(pr)