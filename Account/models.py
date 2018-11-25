from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.forms import ModelForm
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from Profile.models import create_profile
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from time import timezone
import datetime
from django.utils.timezone import utc

YEAR_CHOICES = (
    (2, '2nd'),
    (3, '3rd'),
    (4, '4th'),
)
ROOM_NUMBER = (
    (101, '101'),
    (102, '102'),
    (103, '103'),
    (104, '104'),
    (105, '105'),
    (201, '201'),
    (202, '202'),
    (203, '203'),
    (204, '204'),
    (205, '205'),
    (207, '207'),
    (208, '208'),
    (209, '209'),
    (210, '210'),
    (211, '211'),
    (212, '212'),
    (301, '301'),
    (302, '302'),
    (303, '303'),
    (304, '304'),
    (305, '305'),
    (306, '306'),
    (307, '307'),
    (308, '308'),
    (309, '309'),
    (310, '310'),
    (311, '311'),
    (312, '312'),
)


## custome usermanager
class RBCUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, year='', room_number='', first_name='', middle_name='', last_name='', is_staff=False, is_active=False, is_admin=False, is_authenticated=False, **extra_fields):
        #if not email:
            #raise ValueError("Email not valid")
        #now = timezone.now()
        if not password:
            raise ValueError("Password error")
        if not year:
            raise ValueError("User must have an year")
        if not room_number:
            raise ValueError("User must be in a valid room")
        user_obj = self.model(
            # username = self.get_by_natural_key(username),
            #email = email,
            username=username,
            year = year,
            room_number=room_number,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            **extra_fields,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.authenticated = is_authenticated
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, username, password=None, **extra_fields):
        user = self.create_user(
            username,
            #email,
            password=password,
            is_staff=True,
            **extra_fields,
        )
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(
            username,
            #email,
            password=password,
            is_active=True,
            is_admin=True,
            is_staff=True,
            is_authenticated = True,
            **extra_fields,
        )
        return user


## ## custome usermodel
class RBCUser(AbstractBaseUser):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    username = models.CharField(_('username'),max_length=50, blank=True, null=True, unique=True)
    first_name = models.CharField(_('first_name'),max_length=50, blank=False, null=False)
    middle_name = models.CharField(_('middle_name'),max_length=50, blank=True, null=True)
    last_name = models.CharField(_('last_name'),max_length=50, blank=True, null=True)
    year = models.IntegerField(_('year'),choices=YEAR_CHOICES, null=True,)
    room_number = models.IntegerField(_('room_number'),choices=ROOM_NUMBER, null=True)
    active = models.BooleanField(_('active'),default=False) # can login
    staff = models.BooleanField(_('staff'),default=False) #staff non admin/super
    admin = models.BooleanField(_('admin'),default=False) #admin/superuser
    authenticated = models.BooleanField(_('authenticated'),default=False) # for authentication
    date_joined=models.DateField(_('date_joined'),auto_now_add=True)

    USERNAME_FIELD = 'username'
    # email and password are required
    REQUIRED_FIELDS = ['first_name','middle_name','last_name','year','room_number',]
    # custom user manager
    objects = RBCUserManager()

    class Meta:
        verbose_name=_('user')
        verbose_name_plural = _('users')


    def __str__(self):
        return self.username

    def get_username(self):
        return self.username

    def get_full_name(self):
        '''
                Returns the first_name plus the last_name, with a space in between.
                '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    #def email_user(self):
        #

    #def get_email(self):
        #return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_authenticated(self):
        return self.authenticated

post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)