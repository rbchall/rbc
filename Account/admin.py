from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from .models import RBCUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm,UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    search_fields = ['email', 'username', 'room_number', 'year']
    form = UserAdminChangeForm #edit form
    add_form = UserAdminCreationForm #add form

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin', 'username','year','room_number')
    list_filter = ('admin','year',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('year','room_number','veg')}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('room_number',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

"""
class RBCUserAdmin(admin.ModelAdmin):
    search_fields = ['email','username','room_number','year']
    list_display = ['email','username','room_number','year']
    class Meta:
        model = RBCUser

admin.site.register(User, RBCUserAdmin)
#admin.site.register(RBCUser)
"""