from django.contrib import admin

# Register your models here.

from .models import Hostel, HostelImgScroll, ImageUpload
from .models import AAA as AA


class Hostel_admin_view(admin.ModelAdmin):
    list_display = ('Hostel_name',)


admin.site.register(Hostel, Hostel_admin_view)


class Scroll_image(admin.ModelAdmin):
    list_display = ('Image_description', 'Images_scroll', 'Image_comment', 'Image_priority')


admin.site.register(HostelImgScroll, Scroll_image)


class upload_image(admin.ModelAdmin):
    list_display = ('image_slug', 'image',)

admin.site.register(ImageUpload, upload_image)

class AAA(admin.ModelAdmin):
    list_display = ('Event',)

admin.site.register(AA, AAA)
