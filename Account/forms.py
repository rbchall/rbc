from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import RBCUser, ROOM_NUMBER, YEAR_CHOICES

class SignUP(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    #room_number = forms.ChoiceField(choices=ROOM_NUMBER)
    class Meta:
        model = RBCUser
        fields = [
            'username',
            'email',
            'room_number',
            'year',
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['passsword'] != cd['password2']:
            raise forms.ValidationError("Password do not match")
        return cd['password2']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = self.objects.filter(username=username)
        if r.exists():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = self.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = RBCUser
        fields = [
            'username',
            'email',
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['passsword'] != cd['password2']:
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
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


"""
    def save(self, commit=True):
        user = super(signup, self).save(commit=False )
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password'],
        )
        if commit:
             user.save()

        return user

class UserDetailEditForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('veg_on_egg','veg_on_fish','veg_on_chicken','veg_on_mutton')

class UserMealstatus(forms.ModelForm):
    class Meta:
        model = profile
        fields= ('meal_status',)
"""