from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from social.models import Profile, Post

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
