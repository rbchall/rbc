from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import RBCUser# ROOM_NUMBER, YEAR_CHOICES
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
User = get_user_model()

class SignUP_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    #room_number = forms.ChoiceField(choices=ROOM_NUMBER)
    class Meta:
        model = RBCUser
        fields = [
            'username',
            'first_name',
            'middle_name',
            'last_name',
            #'email',
            'room_number',
            'year',
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password do not match")
        return cd['password2']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = RBCUser.objects.filter(username=username)
        if r.exists():
            raise ValidationError("Username already exists")
        return username

    #def clean_email(self):
     #   email = self.cleaned_data.get('email')
      #  qs = RBCUser.objects.filter(email=email)
       # if qs.exists():
        #    raise forms.ValidationError("email is taken")
        #return email

class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = RBCUser
        fields = [
            'username',
         #   'email',
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Password do not match")
        return cd['password2']

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = RBCUser
        fields = ('username', 'password', 'active', 'admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class Login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RBCUser
        fields = [
            'username',
            'password',
        ]
