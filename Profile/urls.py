from django.urls import path
from . import views
from django.contrib import admin
#from django.contrib.auth import login,logout
from django.contrib.auth import views as authviews

app_name = 'Profile'

urlpatterns=[
    path('', views.view_profile, name='profile_view'),
    path('edit', views.edit_profile, name='profile_edit'),

]