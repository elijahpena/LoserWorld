from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from social.models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'adult'
