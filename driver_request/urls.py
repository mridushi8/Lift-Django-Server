from django.conf.urls import url, include
from .views import driver_request

urlpatterns = [

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^driver_request', driver_request )

]
