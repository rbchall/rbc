from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):

    context={}
    return render(request, 'mess/home.html', context )