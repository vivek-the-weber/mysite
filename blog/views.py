from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import BlogModel,CommentModel
from .forms import CommentForm
class IndexView(ListView):
    model = BlogModel
    template_name = "blog/index.html"
    context_object_name = "recent_blogs"
    ordering = ["-updated_at"]
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
# def index(request):
#     recent_blogs = BlogModel.objects.all().order_by("-updated_at")[:3]
#     return render(request,"blog/index.html",{
#         "recent_blogs" : recent_blogs
#     })

class PostListView(ListView):
    model = BlogModel
    template_name = "blog/all_posts.html"
    context_object_name = "all_blogs"

# def posts_list(request):
#     all_blogs = BlogModel.objects.all()
#     return render(request,"blog/all_posts.html",{
#         "all_blogs" : all_blogs
#     })
class IndividualPostView(View):
    def get(self,request,slug):
        blog = get_object_or_404(BlogModel,slug = slug)
        comment_form = CommentForm()
        all_comments = blog.comments.all()[: : -1]
        return render(request,"blog/detail_post.html",{
            "individual_blog" : blog,
            "post_tags" : blog.tags.all(),
            "comment_form" : comment_form,
            "all_comments" : all_comments,
        })
    def post(self,request, slug):
        temp_filled_form = CommentForm(request.POST)
        blog = get_object_or_404(BlogModel,slug = slug)
        if temp_filled_form.is_valid():
            filled_form = temp_filled_form.save(commit=False)
            filled_form.blog = blog
            filled_form.save()
            redirect_path = reverse("detail-post",args= [slug])
            return HttpResponseRedirect(redirect_path)
        else:
            return render(request,"blog/detail_post.html",{
            "individual_blog" : blog,
            "post_tags" : blog.tags.all(),
            "comment_form" : filled_form,
            })
        
class ReadLaterView(View):
    def get(self,request):
        slug_list = request.session.get("read_later_blogs")
        context = {}
        if slug_list is None or len(slug_list) == 0:            
            context["read_laters"] = []
        else:
            blogs = BlogModel.objects.filter(slug__in = slug_list)
            context["read_laters"] = blogs
        return render(request,"blog/read_later.html",context)
    def post(self,request):
        read_later_blog = request.POST["read_later_blog"]
        slugs_list = request.session.get("read_later_blogs")
        redirect_path = reverse("detail-post",args=[read_later_blog])
        if slugs_list is None:
            slugs_list = []
        if read_later_blog not in slugs_list:
            slugs_list.append(read_later_blog)
            request.session["read_later_blogs"] = slugs_list
        return HttpResponseRedirect(redirect_path)
# def individual_post(request,slug):
#     blog = get_object_or_404(BlogModel,slug=slug)
#     return render(request,"blog/detail_post.html",{
#         "individual_blog" : blog,
#         "post_tags":blog.tags.all(),
#     })
