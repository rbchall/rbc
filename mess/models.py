from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class image_scroll(models.Model):
    Image_description = models.CharField(max_length=100)
    Image_height = models.IntegerField(null=True, blank=True, editable=False, default="300", help_text='300')
    Image_width = models.IntegerField(null=True, blank=True, editable=False, default="700", help_text='700')
    Images_scroll = models.ImageField(upload_to='Mess/Images/', width_field='image_width',
                                      height_field='image_height')
    Image_comment = models.CharField(max_length=100, default="RBC Hall Mess")
    Image_priority = models.IntegerField(default=0)

class secretary(models.Model):
    position=(
        ('secretary', 'secretary'),
        ('Asst.secretary', 'Asst.secretary'),
    )
    portfolio= models.CharField(max_length=10,choices=position)
    name = models.CharField(max_length=50)
    Image_height = models.IntegerField(null=True, blank=True, editable=False, default="100", help_text='100')
    Image_width = models.IntegerField(null=True, blank=True, editable=False, default="100", help_text='100')
    photo = models.ImageField(upload_to='Mess/Images/', width_field='image_width',
                                      height_field='image_height')
    email = models.EmailField(default="")
    Phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10,13}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    PhoneNo = models.CharField(
        max_length=13, validators=[Phone_regex], blank=True)  # validators should be a list