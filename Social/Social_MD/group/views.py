from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.db import IntegrityError

from django.views.generic import ListView,DetailView,CreateView,RedirectView

from group.models import Group,GroupMember

class CreateGroup(CreateView,LoginRequiredMixin,PermissionRequiredMixin):
    fields=('name','description')
    model=Group

    
class SingleGroup(DetailView):
    model=Group

class ListGroup(ListView):
    model=Group


class Joingroup(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})
    
    

         

    def get(self, request, *args, **kwargs):

        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
             messages.warning(self.request,("you not join"))

        else:
            messages.success(self.request,("join the group"))
  

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin,RedirectView):
    
    # def get_redirect_url(self, *args, **kwargs):
    #      return reverse('gruops:single',kwargs={"slug":self.kwargs.get('slug')})
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})
    
    def get(self, request ,*args ,**kwargs):
    
        try:
         mem=GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
         #mem = GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug')).get()
        
        except GroupMember.DoesNotExist:
           
           messages.warning(self.request,"not delete")
        else:
           mem.delete()
           messages.success( self.request,"you cane leave")

        return super().get(request, *args, **kwargs)
    





