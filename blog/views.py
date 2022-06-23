import random

from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Post, Profile, Category


# def index(request):
#     posts = Post.objects.all()
#
#     return render(request, 'index.html', {'posts': posts})

def index(request):
    posts = Post.objects.all()
    random_posts = Post.objects.order_by('id')[:3]
    categories = Category.objects.all()
    for category in categories:  # calculating the amount of posts in each category and assigning special field
        category.posts_count = Post.objects.filter(category__name=category.name).count()

    paginator = Paginator(posts, 6)  # Show 6 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'test.html', {'posts': posts, 'random_posts': random_posts,
                                         'categories': categories, 'page_obj': page_obj})


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'detail.html', {'post': post})


# TODO переделать , плохая практика , код повторяется, заглушка

def category(request, name):
    posts = Post.objects.filter(category__name=name)
    random_posts = Post.objects.order_by('id')[:3]
    categories = Category.objects.all()
    for category in categories:  # calculating the amount of posts in each category and assigning special field
        category.posts_count = Post.objects.filter(category__name=category.name).count()
    paginator = Paginator(posts, 1)  # Show 2 posts per page.
    page_number = request.GET.get(name+'page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'test.html', {'posts': posts, 'random_posts': random_posts,
                                         'categories': categories, 'page_obj': page_obj})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profiles = Profile.objects.all()
    print(profiles)
    return render(request, 'profile.html')
