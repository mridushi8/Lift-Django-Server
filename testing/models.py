from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    pic = models.FileField(null = True, max_length = 10485760)
    phone = models.IntegerField()
    home_add= models.TextField()
    carno= models.CharField(max_length=100)
    identity = models.FileField(null = True, max_length = 10485760)
    password = models.CharField(max_length=100)
    avg_rating = models.CharField(null= True,max_length=100)
    number_of_ratings = models.IntegerField(null = True)

    def __unicode__(self):
        return self.email

    def as_json(self):
        return dict(
            name=self.name,
            email = self.email,
 #           pic = self.pic,
            phone=self.phone,
            home_add =self.home_add,
            carno = self.carno,
 #           identity = self.identity,
            password = self.password,
            avg_rating =self.avg_rating,
            number_of_ratings = self.number_of_ratings
        )
