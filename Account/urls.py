from django.urls import path
from . import views
from django.contrib import admin
#from django.contrib.auth import login,logout
from django.contrib.auth import views as authviews

app_name = 'Account'

urlpatterns=[
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    #path('logout', authviews.logout, {'template_name':'profile/logout.html'}, name='logout'),
    #path('edit', views.edit, name='edit'),
]