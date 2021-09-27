from django.shortcuts import render
from .models import Post

def home_views(request, *args, **kwargs):
    qs = Post.objects.all().order_by('-timestamp')[0:6]
    context = {
        "posts": qs
    }
    return render(request, 'pages/home.html', context)


def blog_list_views(request, *args, **kwargs):
    qs = Post.objects.all()
    context = {
        "posts": qs
    }
    return render(request, 'blog/pages/blog_list.html', context)