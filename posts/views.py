from django.shortcuts import render
from .models import Post
import datetime

# Create your views here.

def index(request):
    posts = Post.objects.raw('SELECT * FROM post')
    print("posts are:",posts)
    return render(request, 'index.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.raw('SELECT * FROM post WHERE post_id = '+ str(post_id))
    print("post is:",post)
    return render(request, 'post.html', {'post': post})