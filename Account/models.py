from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

YEAR_CHOICES = (
    (2, '2nd'),
    (3, '3rd'),
    (4, '4th'),
)
ROOM_NUMBER = (
    (101, '101'),
    (102, '102'),
    (103, '103'),
    (202, '202'),
    (211,'211'),
)


## custome usermanager
class RBCUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_staff=False, is_active=False, is_admin=False):
        if not email:
            raise ValueError("Email not valid")
        if not password:
            raise ValueError("Password error")
        user_obj = self.model(
            email=self.normalize_email(email),
            # username = self.get_by_natural_key(username),
            username=username
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staff(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            username,
            password=password,
            is_active=True,
            is_admin=True,
            is_staff=True,
        )
        return user


## ## custome usermodel
class RBCUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, null=True)
    room_number = models.IntegerField(choices=ROOM_NUMBER, null=True)
    veg = models.BooleanField(default=False)
    active = models.BooleanField(default=False) # can login
    staff = models.BooleanField(default=False) #staff non admin/super
    admin = models.BooleanField(default=False) #admin/superuser

    USERNAME_FIELD = 'email'
    # email and password are required
    REQUIRED_FIELDS = ['username',]
    # custom user manager
    objects = RBCUserManager()

    def __str__(self):
        return self.email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

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
