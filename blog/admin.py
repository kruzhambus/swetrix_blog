from django.contrib import admin
from blog.models import Post, Profile, Category, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
