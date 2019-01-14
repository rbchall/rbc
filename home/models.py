from distutils.command.upload import upload

from django.core.validators import RegexValidator
from django.db import models
from isort.settings import default


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
    Description_for_seo = models.TextField(max_length=255,blank=True,null=True,help_text="Decription of page for seo")
    author_of_page = models.CharField(blank=True,null=True,max_length=25)
    Facebook= models.URLField(help_text="url to facebook page, default = https://www.facebook.com/Rishi-Bankim-Chandra-HallKGEC-105289579543000/ ", default="https://www.facebook.com/Rishi-Bankim-Chandra-HallKGEC-105289579543000/")
    Twitter=models.URLField(help_text="twitter link, default = https://twitter.com/kgecrbchall", default="https://twitter.com/kgecrbchall")
    Google_Plus =models.URLField(help_text="google+ default url:- https://plus.google.com/u/5/", default="https://plus.google.com/u/5/")
    Youtube = models.URLField(help_text="youtube channel default:-https://www.youtube.com/channel/UC3JOr-Opub8GRKwJjktqZtA", default="https://www.youtube.com/channel/UC3JOr-Opub8GRKwJjktqZtA")

    def __str__(self):
        return "{}".format(self.Hostel_name)


class HostelImgScroll(models.Model):
    Image_description = models.CharField(max_length=100)
    image_height = models.IntegerField(null=True, blank=True, editable=False, default="1080", help_text='prefered: 1080')
    image_width = models.IntegerField(null=True, blank=True, editable=False, default="1900", help_text='prefered: 1900')
    Images_scroll = models.ImageField(upload_to='Hostel/Images/', width_field='image_width',
                                      height_field='image_height')
    Image_comment = models.CharField(max_length=100, default="KGEC", help_text="for SEO")
    Image_priority = models.IntegerField(default=0)
    #def __str__(self):
    #    return "{}".format(self.Image_comment)

class ImageUpload(models.Model):
    image= models.ImageField(upload_to='Hostel/Images/')
    image_description= models.CharField(max_length=100)
    image_slug= models.CharField(max_length=10, null=False, blank=False, default="R.B.C Hall", help_text="slug to identify image for seo, keep different")

AAA_CHOICES = (
    ('Accoglienza', 'Accoglienza'),
    ('Alfresco', 'Alfresco'),
    ('Alvida', 'Alvida'),
)
AAA_priotity = (
    (1, 'Accoglienza'),
    (2, 'Alfresco'),
    (3, 'Alvida'),
)

class AAA(models.Model):
    Event = models.CharField(max_length=20,choices=AAA_CHOICES,blank=False,null=True)
    description = models.TextField(max_length=255,blank=False,null=False)
    Event_Image = models.ImageField(upload_to='AAA/', default='image.png')
    Image_Comment = models.CharField(max_length=20,blank=False,null=True)
    url = models.URLField(help_text="if a page exists for the event then enter or leave '#' ", blank=True, null=True)

    def __str__(self):
        return "{}".format(self.Event)
