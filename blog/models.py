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


class Post(models.Model):
    title = models.CharField(max_length=255)
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.TextField(max_length=60, default="Anonymous", blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    # dislikes = models.ManyToManyField(User, related_name='comment_dislikes', blank=True)

    def __str__(self):
        return self.author
