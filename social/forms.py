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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'post']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CommentCreateForm, self).__init__(*args, **kwargs)
