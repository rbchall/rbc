from django.shortcuts import render

# Create your views here.
from home.models import Hostel
from django.shortcuts import get_object_or_404
from .models import *
from Profile.models import UserProfile

def home(request):
    hostel = get_object_or_404(Hostel, slug="RBC")
    profiles = UserProfile.objects.all()
    title = "Mess"
    total = 0
    veg = 0
    fish = 0
    egg = 0
    chicken = 0
    mutton = 0
    for profile in profiles:

        if profile.meal_status==True:
            total =+ 1
            ## for veg
            if profile.veg == True:
                veg = + 1
            else:
                veg = veg

            ## for fish
            if profile.veg_on_fish == True:
                fish = + 1
            else:
                fish = fish

            ##for egg
            if profile.veg_on_egg == True:
                egg = + 1
            else:
                egg = egg

            ##for chicken
            if profile.veg_on_chicken == True:
                chicken = + 1
            else:
                chicken = chicken

            ##for mutton
            if profile.veg_on_mutton == True:
                mutton = + 1
            else:
                mutton = mutton
        else:
            total = total


    context={
        "title": title,
        'hostel': hostel,
        'total':total,
        'veg':veg,
        'fish':fish,
        'egg':egg,
        'Chicken':chicken,
        'mutton':mutton,
    }
    return render(request, 'mess/home.html', context )