from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Hostel(models.Model):
    Hostel_name = models.CharField(max_length=50, primary_key=True)
    Hostel_short = models.CharField(max_length=10, default="")
    slug = models.SlugField(max_length=10, unique=True, default='',
                            help_text='enter the filed with hostel short as RBC')
    Hostel_Email = models.EmailField(default="")
    Phone_regex= RegexValidator(
        regex=r'^\+?1?\d{10,13}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    PhoneNo = models.CharField(
        max_length=13, validators=[Phone_regex], blank=True)  # validators should be a list
    Hostel_startdate = models.DateField(auto_now=False)
    image_height = models.IntegerField(null=True, blank=True, editable=False, default="100", help_text='100')
    image_width = models.IntegerField(null=True, blank=True, editable=False, default="100", help_text='100')
    Hostel_logo = models.ImageField(upload_to='Hostel/Logo/', width_field='image_width', height_field='image_height')
    Hostel_description = models.TextField()
    Facebook= models.URLField(help_text="url to facebook page, default = https://www.facebook.com/Rishi-Bankim-Chandra-HallKGEC-105289579543000/ ", default="https://www.facebook.com/Rishi-Bankim-Chandra-HallKGEC-105289579543000/")
    Twitter=models.URLField(help_text="twitter link, default = https://twitter.com/kgecrbchall", default="https://twitter.com/kgecrbchall")
    Google_Plus =models.URLField(help_text="google+ default url:- https://plus.google.com/u/5/", default="https://plus.google.com/u/5/")
    Youtube = models.URLField(help_text="youtube channel default:-https://www.youtube.com/channel/UC3JOr-Opub8GRKwJjktqZtA", default="https://www.youtube.com/channel/UC3JOr-Opub8GRKwJjktqZtA")

    # def __str__(self):
    #    return "{}".format(self.id,self.Hostel_name)


class Hostel_img_scroll(models.Model):
    Image_description = models.CharField(max_length=100)
    image_height = models.IntegerField(null=True, blank=True, editable=False, default="300", help_text='300')
    image_width = models.IntegerField(null=True, blank=True, editable=False, default="700", help_text='700')
    Images_scroll = models.ImageField(upload_to='Hostel/Images/', width_field='image_width',
                                      height_field='image_height')
    Image_comment = models.CharField(max_length=100, default="KGEC")
    Image_priority = models.IntegerField(default=0)

class image_upload(models.Model):
    image= models.ImageField(upload_to='Hostel/Images/')
    image_description= models.CharField(max_length=100)
    image_slug= models.CharField(max_length=10, null=False, blank=False, default="R.B.C Hall", help_text="slug to identify image for seo, keep different")
