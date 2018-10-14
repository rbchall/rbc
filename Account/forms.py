from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class signup(forms.Form):
    username = forms.CharField(label='username',max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fileds = ['username','first_name','Last_name']

    class Meta:
        model =UserDetails
        fileds = ['room_number','year']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['passsword'] != cd['password2']:
            raise forms.ValidationError("Password do not match")
        return cd['password2']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password']
        )
        return user

class UserDetailEditForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('veg','veg_on_egg','veg_on_fish','veg_on_chicken','veg_on_mutton','room_number','year')

class UserMealstatus(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields= ('meal_status',)
