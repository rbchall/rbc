from django.contrib import admin

# Register your models here.

from .models import *


class Hostel_admin_view(admin.ModelAdmin):
    list_display = ('Hostel_name',)


admin.site.register(Hostel, Hostel_admin_view)


class Scroll_image(admin.ModelAdmin):
    list_display = ('Image_description', 'Images_scroll', 'Image_comment', 'Image_priority')


admin.site.register(Hostel_img_scroll, Scroll_image)


class upload_image(admin.ModelAdmin):
    list_display = ('image_slug', 'image',)

admin.site.register(image_upload, upload_image)

