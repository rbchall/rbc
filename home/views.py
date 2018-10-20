from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Hostel, HostelImgScroll, ImageUpload

def index(request):
    hostel=get_object_or_404(Hostel, slug="RBC")
    hostel_scrool_image= HostelImgScroll.objects.all().order_by('Image_priority')
    context={'hostel': hostel, 'hostel_scroll_img': hostel_scrool_image}
    return render(request,'home/home.html', context)
