from django.urls import path
from django.contrib.auth import views as Auth_view
from . import views



app_name="accounts"
urlpatterns = [
    path('login/',Auth_view.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',views.custom_logout,name='logout'),
    path("sginup/",views.Sidnup.as_view(),name='signup')
]
