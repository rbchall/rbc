from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings

YEAR_CHOICES=(
    ('2', '2nd'),
    ('3', '3rd'),
    ('4', '4th'),
)
ROOM_NUMBER=(
    ('101','101'),
    ('102', '102'),
    ('103', '103'),
    ('202', '202'),
)


class UserDetails(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='UserDetails', on_delete=models.CASCADE)
    meal_status= models.BooleanField(default=True)
    veg = models.BooleanField(default=False)
    veg_on_egg = models.BooleanField(default=False)
    veg_on_fish = models.BooleanField(default=False)
    veg_on_chicken =models.BooleanField(default=False)
    veg_on_mutton = models.BooleanField(default=False)
    year= models.IntegerField(choices=YEAR_CHOICES)
    room_number= models.IntegerField(choices=ROOM_NUMBER)