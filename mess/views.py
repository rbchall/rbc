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
    for profile in profiles:
        total=0
        if profile.meal_status==True:
            total =+ 1
        else:
            total = total

        ## for veg
        veg = 0
        if profile.veg == True:
            veg = + 1
        else:
            veg = veg

        ## for fish
        fish = 0
        if profile.veg_on_fish == True:
            fish = + 1
        else:
            fish = fish

        ##for egg
        egg = 0
        if profile.veg_on_egg == True:
            egg = + 1
        else:
            egg = egg

        ##for chicken
        chicken = 0
        if profile.veg_on_chicken == True:
            chicken = + 1
        else:
            chicken = chicken

        ##for mutton
        mutton = 0
        if profile.veg_on_mutton == True:
            mutton = + 1
        else:
            mutton = mutton

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