from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from social.models import Profile, Post, Comment

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

