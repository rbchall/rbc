from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.

from django.shortcuts import redirect
from .forms import SignUP_form,Login_form
from .models import RBCUser
from home.models import Hostel
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

user = get_user_model()

def signup_view(request):
    title = "Signin"
    hostel = get_object_or_404(Hostel, slug="RBC")
    context ={
        "title": title,
        'hostel': hostel
    }
    if request.method == 'POST':
        form = SignUP_form(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            messages.success(request, 'Account created successfully')
            form = SignUP_form()
            return redirect('/login')

    else:
        form = SignUP_form()
        #context = {'form':form}
        context.update({'form':form})
    return render(request, 'Account/signup.html',context)

def login_view(request):
    title = "Login"
    hostel = get_object_or_404(Hostel, slug="RBC")
    context = {
        "title":title,
        'hostel': hostel
    }
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your Rango account is disabled.")
            else:
                return HttpResponse("Invalid login details supplied.")
    else:
        form = Login_form()
    context.update({"form": form})
    return render(request, 'Account/signup.html', context)

def logout_view(request):
    title = "Logout"
    hostel = get_object_or_404(Hostel, slug="RBC")
    logout_text = "You have succesfully Logged out"
    context = {
        "title": title,
        "logout_text": logout_text,
        'hostel': hostel
    }
    logout(request)
    return render(request, 'Account/logout.html', context)

def dual(request):
    hostel = get_object_or_404(Hostel, slug="RBC")
    form1 = Login_form()
    form2 = SignUP_form()
    context={
        'hostel': hostel,
        "form_login": form2,
        'form_signup': form1,
    }
    return render(request, 'Account/dual.html', context)