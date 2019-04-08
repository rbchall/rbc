from django.contrib import admin

# Register your models here.
from .models import NetProfile,MAC_Id

class NetProfile_admin_view(admin.ModelAdmin):
	class Meta:
		model = NetProfile
	search_fields = ['user','Amount_Due']
	list_display = ('user','Amount_Due')
	list_filter = ('user','Amount_Due')

admin.site.register(NetProfile, NetProfile_admin_view)

class MAC_admin_view(admin.ModelAdmin):
	class Meta:
		model = MAC_Id
	search_fields = ['Name','Physical_Address','IP_Address']
	list_display = ('Name','Physical_Address','IP_Address')
	list_filter = ('Name','Physical_Address','IP_Address')

admin.site.register(MAC_Id, MAC_admin_view)