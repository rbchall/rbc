from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .forms import SignUP

def signup(request):
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            form = SignUP()
            return redirect('/')

    else:
        form = SignUP()
        context = {'form':form}
    return render(request, 'Account/signup.html',context)
