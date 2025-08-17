from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("posts/",views.posts_list, name="all-posts"),
    path("posts/<slug:slug>",views.individual_post, name="detail-post")
]

