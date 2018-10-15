from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import RBCUser

class signup(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    class Meta:
        model = RBCUser
        fields = ['room_number','year','veg']

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
        user = super(signup, self).save(commit=False )
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password'],
        )
        if commit:
             user.save()

        return user

"""
class UserDetailEditForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('veg_on_egg','veg_on_fish','veg_on_chicken','veg_on_mutton')

class UserMealstatus(forms.ModelForm):
    class Meta:
        model = profile
        fields= ('meal_status',)
"""