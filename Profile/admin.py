from django.contrib import admin
from .models import UserProfile
from Account.models import RBCUser
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()

class Profile_admin_view(admin.ModelAdmin):
    class Meta:
        model = User
    search_fields = ['user','meal_status','veg_on_egg','veg','veg_on_fish','veg_on_mutton','veg_on_chicken']
    list_display = ('user','fine','meal_status','veg','veg_on_egg','veg_on_mutton','veg_on_fish','veg_on_chicken')
    list_filter = ('meal_status','veg','veg_on_fish','veg_on_mutton','veg_on_egg','veg_on_chicken')
    ordering = ()
    filter_horizontal = ()

admin.site.register(UserProfile, Profile_admin_view)