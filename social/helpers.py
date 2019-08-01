from django.core.exceptions import PermissionDenied
from .models import User, Profile, Post, Comment

def is_owner(post, user):
    if post.user == user:
        return True
    
    return False
