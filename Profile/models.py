from django.conf import settings
from django.contrib.auth import get_user_model
# from Account.models import RBCUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.template.base import kwarg_re


# content_room= ContentType.objects.get_for_model(RBCUser.room_number)
# content_year=ContentType.objects.get_for_model(RBCUser.year)

# permission = Permission.objects.create(
#    codename='can_edit',
#    name='can edit profile account',
#    content_type=[content_room,content_year],
# )

# User = get_user_model()

# @login_required
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='UserDetails', on_delete=models.CASCADE)
    # room_number = models.ForeignKey('Account.RBCUser.room_number', on_delete=models.CASCADE)
    #username = models.ForeignKey(settings.AUTH_USER_MODEL,default=user, on_delete=models.CASCADE)
    veg = models.BooleanField(default=False)
    meal_status = models.BooleanField(default=False)
    veg_on_egg = models.BooleanField(default=False)
    veg_on_fish = models.BooleanField(default=False)
    veg_on_chicken = models.BooleanField(default=False)
    veg_on_mutton = models.BooleanField(default=False)
    fine = models.IntegerField(blank='', null='', default='0')

    # def __str__(self):
    #    return self.user


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
