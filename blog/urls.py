from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("posts/",views.PostListView.as_view(), name="all-posts"),
    path("posts/<slug:slug>",views.IndividualPostView.as_view(), name="detail-post")
]

