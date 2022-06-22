from django.shortcuts import render

from .models import Post, Profile


# def index(request):
#     posts = Post.objects.all()
#
#     return render(request, 'index.html', {'posts': posts})

def index(request):
    posts = Post.objects.all()
    return render(request, 'test.html', {'posts': posts})


def detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'detail.html', {'post': post})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profiles = Profile.objects.all()
    print(profiles)
    return render(request, 'profile.html')
