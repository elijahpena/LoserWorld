from django.core.exceptions import PermissionDenied
from .models import User, Profile, Post, Comment

def is_owner(obj, user):
    if obj.user == user:
        return True
    
    return False
