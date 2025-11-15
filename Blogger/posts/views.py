from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.


def create_post_view(request:HttpRequest):


    if request.method=="POST":
        new_post = Post(title=request.POST["title"], content= request.POST["content"], is_published= request.POST["is_published"], published_at= request.POST["published_at"])
        new_post.save()

    return render(request, 'posts/create.html')