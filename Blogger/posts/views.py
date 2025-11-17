from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.


def create_post_view(request:HttpRequest):

    post_form=PostForm()

    if request.method=="POST":
        post_form=PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('main:home_view')
        return render(request, 'posts/create.html', {'form': post_form})

    return render(request, 'posts/create.html')

def post_detail_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)

    return render(request, 'posts/post_detail.html', {"post":post})

def post_update_view(request:HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        post_form=PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:post_detail_view', post_id=post.id)
        return render(request, 'posts/update_post.html', {'form': post_form, 'post': post})
    post_form = PostForm(instance=post)

    return render(request, 'posts/update_post.html', {"post": post})

def post_delete_view(request:HttpRequest, post_id:int):

    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect("main:home_view")

def all_posts_view(request:HttpRequest):

    post = Post.objects.all().order_by("-published_at")
    return render(request, 'posts/all_posts.html', {'post': post})

def search_post_view(request:HttpRequest):
    query = request.GET.get('search', '').strip()
    order_by= request.GET.get('order_by','')
    
    if query:
        posts = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            content__icontains=query
        )
    else:
        posts = Post.objects.none()

    if order_by == 'draft':
        posts = posts.filter(is_published=False)
    elif order_by == 'published':
        posts = posts.filter(is_published=True)
    elif order_by == 'newest':
        posts = posts.order_by('-published_at')
    elif order_by == 'oldest':
        posts = posts.order_by('published_at')
    
    return render(request, 'posts/search_post.html', {"posts": posts, "query": query, "order_by":order_by})
