from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
#from .models import *
from .forms import signup

def signup(request):
    if request.method == 'POST':
        form = signup(request.POST)
        #detailed_form = UserDetailEditForm(request.POST)
        if form.is_valid():
            #user=form.save(commit=False)
            #user=form.cleaned_data['username']
            #password=form.cleaned_data['password']
            #user.set_password(password)
            form.save()
            #userdetail = UserDetails.objects.create(user_id=user.id)
            messages.success(request, 'Account created successfully')
            return redirect('Account/signup')

    else:
        form = signup()
        context = {'form':form}
    return render(request, 'Account/signup.html',context)

            #user = authenticate(username=username,password=password)
            #if user is not None:
            #    if user.is_active:
            #        login(request,user)
            #        return redirect('')