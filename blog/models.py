import re

from django.contrib.auth.models import User
from django.db import models

from blog.utils import random_photo


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=random_photo("static/images/user_profiles_jpg/"),
                               upload_to='static/images/user_profiles_jpg')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Custom class for the Post model
class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        # replace all special symbols with spaces in the string
        value = re.sub(r'[^\w]', ' ', value)
        new_str = str(value).lower().replace(' ', '-').replace('?', '-').strip().replace("'", '').replace('--', '-')
        return new_str[:-1] if new_str[-1] == '-' else new_str


class Post(models.Model):
    title = models.CharField(max_length=255)
    url_path = NameField(max_length=255, null=True, blank=True)
    intro = models.TextField(max_length=90)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    preview_photo = models.ImageField(default=random_photo("static/images/post_preview"),
                                      upload_to='static/images/post_preview')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80, default='')
    email = models.EmailField(null=True, blank=True, default='')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
