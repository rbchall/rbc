from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from Account.models import RBCUser
from .models import UserProfile
from django.contrib.auth import get_user_model

User= get_user_model()

class Profile_edit_form(forms.ModelForm):
    class Meta:
        models = UserProfile
        exclude =[
            'user',
            'fine',

        ]