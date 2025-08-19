from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import BlogModel

def index(request):
    recent_blogs = BlogModel.objects.all().order_by("-updated_at")[:3]
    return render(request,"blog/index.html",{
        "recent_blogs" : recent_blogs
    })

def posts_list(request):
    all_blogs = BlogModel.objects.all()
    return render(request,"blog/all_posts.html",{
        "all_blogs" : all_blogs
    })

def individual_post(request,slug):
    blog = get_object_or_404(BlogModel,slug=slug)
    return render(request,"blog/detail_post.html",{
        "individual_blog" : blog,
        "post_tags":blog.tags.all(),
    })