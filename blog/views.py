from django.shortcuts import render
from .models import Post
from django.http import Http404


def post_list(request):
    """List all posts"""
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', { 'posts': posts })

def post_detial(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    return render(request, 'blog/post/detial.html', { 'post': post })