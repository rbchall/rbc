from django.contrib.auth import get_user_model
# from Account.models import RBCUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.template.base import kwarg_re
from django.conf import settings

class NetProfile(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='NetDetails', on_delete=models.CASCADE)
    Date_Joined = models.DateField(auto_now_add=True)
    Amount_Due = models.IntegerField(default="0", null=False, blank=False)
    Last_Amount_Paid = models.PositiveIntegerField(default="0", null=True, blank=True)
    Last_Amount_Paid_Date = models.DateField(blank=False, null=True)

    def __str__(self):
    	return self.user.username

def create_Netprofile(sender, **kwargs):
    if kwargs['created']:
        user_profile = NetProfile.objects.create(user=kwargs['instance'])

class MAC_Id(models.Model):
    """
    Description: Model Description
    """
    lapi = 'Laptop'
    mob = 'Mobile'
    Device_Choices = (
    	(lapi, 'Laptop'),
    	(mob, 'Mobile'),
    )

    Physical_Address = models.CharField(max_length=12, unique=True)
    Device = models.CharField(choices = Device_Choices,default = lapi,max_length=6)
    Description = models.CharField(max_length=10)
    IP_Address = models.GenericIPAddressField(unique=True)
    Name = models.ForeignKey(NetProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return_text = '%s %s %s' %(self.Name.username,self.Device,self.Description)
    	return return_text