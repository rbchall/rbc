from django.urls import path

from . import views

app_name = 'mess'

urlpatterns=[
    path('', views.home, name='home')
]