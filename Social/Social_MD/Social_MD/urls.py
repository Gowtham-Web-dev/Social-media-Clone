"""
URL configuration for Social_MD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Social_MD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='home'),
    path('accounts/',include('Social.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('test/',views.Testpage.as_view(),name='test'),
    path('thank/',views.Thanks.as_view(),name='thank'),
    path('post/',include('post.urls',namespace='posts')),
    path("group/",include('group.urls',namespace='groups')),    
]
