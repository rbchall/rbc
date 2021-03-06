from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from home.models import Hostel
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import (
    get_user_model,
)
from django.contrib.auth.decorators import login_required
from .forms import Profile_edit_form
from .models import UserProfile

# Create your views here.

User = get_user_model()


@login_required(login_url='/login')
def view_profile(request):
    hostel = get_object_or_404(Hostel, slug="RBC")
    profile = get_object_or_404(UserProfile, user=request.user)
    title = str(request.user) + " Profile"
    context = {
        "title": title,
        'hostel': hostel,
        'user': request.user,
        'User':profile,
    }
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/login')
def edit_profile(request):
    hostel = get_object_or_404(Hostel, slug="RBC")
    title = "edit " + str(request.user) + " Profile"
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        "title": title,
        'hostel': hostel,
        'user': request.user,
        'User': profile,
    }
    if request.method == "POST":
        form = Profile_edit_form(request.POST, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('/profile')
    else:
        form = Profile_edit_form(instance=profile)
        context = {
            "title": title,
            'hostel': hostel,
            'user': request.user,
            'form': form,
            'User': profile,
        }
    return render(request, 'profile/edit_profile.html', context)
