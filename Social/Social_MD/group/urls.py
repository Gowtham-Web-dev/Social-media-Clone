from django.urls import path
from group import views



app_name="groups"
urlpatterns = [
   path('',views.ListGroup.as_view(),name="all"),
   path("new/",views.CreateGroup.as_view(),name="create"),
   path('post/<slug>',views.SingleGroup.as_view(),name="single"),
   path('jon/<slug>',views.Joingroup.as_view(),name="join"),
   path("leave/<slug>",views.LeaveGroup.as_view(),name="leave")
]

