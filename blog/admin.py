from django.contrib import admin
from blog.models import Post, Profile, Category, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)
