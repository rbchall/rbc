from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .forms import SignUP
from home.models import Hostel
from django.shortcuts import render, get_object_or_404

def signup(request):
    hostel = get_object_or_404(Hostel, slug="RBC")
    context ={'hostel': hostel}
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            form = SignUP()
            return redirect('/')

    else:
        form = SignUP()
        context.update({'form':form})
    return render(request, 'Account/signup.html',context)
