from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.


def create_post_view(request:HttpRequest):


    if request.method=="POST":
        new_post = Post(
            title=request.POST["title"], 
            content= request.POST["content"], 
            is_published= request.POST["is_published"], 
            published_at= request.POST["published_at"],    
        )
        if 'image' in request.FILES:
            new_post.image = request.FILES['image']
        
        new_post.save()

        return redirect('main:home_view')

    return render(request, 'posts/create.html')

def post_detail_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    return render(request, 'posts/post_detail.html', {"post":post})

def post_update_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    if request.method=="POST":
            post.title=request.POST["title"], 
            post.content= request.POST["content"], 
            post.is_published= request.POST["is_published"], 
            post.published_at= request.POST["published_at"], 

            if "image" in request.FILES: post.image= request.FILES["image"]
            post.save()

            return redirect('posts:post_detail_view', post_id=post.id)

    return render(request,'posts/update_post.html', {"post":post})

def post_delete_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:home_view")