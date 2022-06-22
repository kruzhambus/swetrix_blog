from django.contrib.auth.models import User
from django.db import models

from blog.utils import random_user_photo


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=random_user_photo("static/images/user_profiles_jpg/"),
                               upload_to='static/images/user_profiles_jpg')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    preview_photo = models.ImageField(default=random_user_photo("static/images"),
                                      upload_to='static/images/post_preview')
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
