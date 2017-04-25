from django.conf import settings
from django.conf.urls import url, include
#from django.conf.urls import patterns
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from passenger_requests.views import passenger_request,get_status,get_driver,get_passenger,driver_response,accept_driver, check_flag, check_payment
from testing.views import checkmatch,register,checkproof,picupload,forgetpass, getAvgRating
from example.estimatedFareCalculationModule import getEstFare
from example.actualFareCalculationModule import getActFare
from driver_request.views import driver_request, player_id, end_journey, complete, start_journey

# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^checkmatch$', checkmatch),
    url(r'^register$', register),
    url(r'^checkproof$', checkproof),
    url(r'^picupload$', picupload),
    url(r'^forgetpass$', forgetpass),

    url(r'^rating', getAvgRating),

    url(r'^driver_request', driver_request),
    url(r'^player_id', player_id),
    url(r'^end_journey', end_journey),
    url(r'^start_journey', start_journey),
    url(r'^complete', complete),
    url(r'^flag',check_flag),

    url(r'^passenger_request', passenger_request),
    url(r'^status', get_status),
    url(r'^get_driver', get_driver),
    url(r'^driver_response', driver_response),
    url(r'^passenger_complete', complete),
    url(r'^get_passenger',get_passenger),
    url(r'^accept_driver', accept_driver),
    url(r'^estimatefare', getEstFare),
    url(r'^actualfare', getActFare),
    url(r'^check_payment',check_payment)
]
