from django.urls import path, reverse
from . import views
from Account.views import login_view, signup_view, logout_view, dual

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
    path('logout', logout_view, name='logout'),
]