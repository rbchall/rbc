from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.

from django.shortcuts import redirect
from .forms import SignUP_form,Login_form
from home.models import Hostel
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

def signup_view(request):
    title = "Signin"
    hostel = get_object_or_404(Hostel, slug="RBC")
    context ={
        "title": title,
        'hostel': hostel
    }
    if request.method == 'POST':
        form = SignUP_form(request.POST)
        print(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.active=True
            user.staff=False
            user.admin=False
            user.authenticated=False
            user.save()
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
            user = authenticate(username=username, password=password)
            if user:
                if user.authenticated:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your account is NOT authenticated.")
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