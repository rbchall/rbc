from django.db import models

# Create your models here.
from Account.models import RBCUser
from django.conf import settings


class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='UserDetails', on_delete=models.CASCADE)
    meal_status = models.BooleanField(default=True)
    veg_on_egg = models.BooleanField(default=False)
    veg_on_fish = models.BooleanField(default=False)
    veg_on_chicken = models.BooleanField(default=False)
    veg_on_mutton = models.BooleanField(default=False)
