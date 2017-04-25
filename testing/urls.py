from django.conf.urls import url, include
from . import views
urlpatterns = [
   
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^checkmatch$', views.checkmatch, name='checkmatch'),
    url(r'^register$', views.register, name='register'),
    url(r'^checkproof$', views.checkproof, name='checkproof'),
    url(r'^picupload$', views.picupload, name='picupload'),
    url(r'^forgetpass$', views.forgetpass, name='forgetpass')


]
