import os
import random
import re

from django import forms
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Post, Profile, Category, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


def index(request):
    posts = Post.objects.all()
    random_posts = Post.objects.order_by('id')[:3]
    categories = Category.objects.all()
    for category in categories:  # calculating the amount of posts in each category and assigning special field
        category.posts_count = Post.objects.filter(category__name=category.name).count()

    paginator = Paginator(posts, 4)  # Show 6 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'test.html', {'posts': posts, 'random_posts': random_posts,
                                         'categories': categories, 'page_obj': page_obj})


# def detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'detail.html', {'post': post})


# TODO переделать , плохая практика , код повторяется, заглушка

def category(request, name):
    random_posts = Post.objects.order_by('id')[:3]
    categories = Category.objects.all()
    for category in categories:  # calculating the amount of posts in each category and assigning special field
        category.posts_count = Post.objects.filter(category__name=category.name).count()
    print("{name}".format(name=name))
    posts = Post.objects.filter(category__name=name)
    print("The categorized posts are : ", posts)
    paginator = Paginator(posts, 2)  # Show 2 posts per page.
    page_number = request.GET.get(name + 'page')
    print(page_number)
    page_obj = paginator.get_page(page_number)
    print("Page obJ is: ", page_obj)
    return render(request, 'category.html', {'posts': posts, 'random_posts': random_posts,
                                             'categories': categories, 'page_obj': page_obj})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profiles = Profile.objects.all()
    print(profiles)
    return render(request, 'profile.html')


def get_post(request, url_path: str, name=None):
    print(url_path)
    # get the post by url path
    # post = Post.objects.get(url_path__startswith=url_path)
    post = Post.objects.get(url_path__exact=url_path)
    # post = Post.objects.get(url_path_s=url_path)
    comments = post.comments.filter(active=True)
    categories = Category.objects.all()
    # получить фото автора
    author_photo = Profile.objects.get(user=post.author.user)
    print(author_photo)
    for category in categories:  # calculating the amount of posts in each category and assigning special field
        category.posts_count = Post.objects.filter(category__name=category.name).count()
    random_posts = Post.objects.order_by('id')[:3]

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect('http://127.0.0.1:8000/post/{url_path}/'.format(url_path=url_path))
    else:
        comment_form = CommentForm()

    return render(request, 'test_detail.html',
                  {'post': post, 'comments': comments, 'comment_form': comment_form, 'random_posts': random_posts,
                   'categories': categories, 'author_photo': author_photo})
