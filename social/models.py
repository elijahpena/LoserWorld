from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    adult = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    posted_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.FileField(blank=True, upload_to='%Y/%m/%d')

    class Meta:
        ordering = ['-posted_on']

    def get_absolute_url(self):
        return reverse('social:post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    posted_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.FileField(blank=True, upload_to='%Y/%m/%d')

    class Meta:
        ordering = ['-posted_on']

    def get_absolute_url(self):
        return reverse('social:comment_detail', args=[str(self.post.id), str(self.id)])
    
    def __str__(self):
        return self.content
