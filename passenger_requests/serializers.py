from rest_framework import serializers
from passenger_requests.models import Trip_Request
from testing.models import User

class TripRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip_Request
        fields = ('request_id','status','driver_id')

'''class UserSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=100)
        email = serializers.EmailField()
        pic = serializers.FileField()
        phone = serializers.IntegerField()
        home_add = serializers.CharField(max_length=100)
        carno = serializers.CharField(max_length=100)
        identity = serializers.FileField()
        password = serializers.CharField(max_length=100)
        rating = serializers.DecimalField(max_digits=4, decimal_places=2)'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email','phone','home_add','carno','identity','password','rating')
