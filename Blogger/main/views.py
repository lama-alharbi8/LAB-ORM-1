from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from posts.models import Post

def home_view(request:HttpRequest):

    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'main/home.html', {'posts': posts})

def mode_view(request: HttpRequest, mode):
    response = redirect(request.GET.get("page", '/'))

    if mode == "dark":
        response.set_cookie("mode", "dark", max_age=60*60*24*7)
    elif mode == "light":
        response.set_cookie("mode", "light", max_age=-3600)

    return response