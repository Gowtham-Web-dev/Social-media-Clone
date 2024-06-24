from django.urls import path
from . import views



app_name="posts"
urlpatterns = [
    path("", views.Postlist.as_view(),name="all"),
    path("new/",views.createpost.as_view(),name="create"),
    path("by/<username>/",views.userpost.as_view(),name="for_user"),
    path("by/<username>/<pk>",views.PostDetail.as_view(),name="single"),
    # path("by/<username>/<pk>", views.PostDetail.as_view(), name="single"),
    path("delete/<pk>/",views.deletePost.as_view(),name="delete")
]
