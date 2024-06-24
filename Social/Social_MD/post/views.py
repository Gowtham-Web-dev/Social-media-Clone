from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.http import Http404, HttpRequest, HttpResponse
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models
from post.models import Post
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


class Postlist(generic.ListView,SelectRelatedMixin):
    model=models.Post
    select_related=('user','group')
    
class userpost(generic.ListView):

    model=models.Post
    template_name="post/user_post_list.html"


    
    def get_queryset(self):
        try:
            self.post_user=User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
            
        except User.DoesNotExist:
              raise Http404
        else:
            return self.post_user.posts.all()
        
    def get_context_data(self, **kwargs):
         context= super().get_context_data(**kwargs)
         context['Post_user']=self.post_user
         return context
class PostDetail(SelectRelatedMixin,generic.DetailView):
     model=Post
     select_related=('user','group')
     def get_queryset(self):
          
          querySet= super().get_queryset()

          return querySet.filter(user__username__iexact=self.kwargs.get('username'))  
     
class createpost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
     fields=('message','group')

     model=models.Post
     template_name='post/post_form.html'

     def form_valid(self,form):
          self.object=form.save(commit=False)
          self.object.user=self.request.user
          self.object.save()
          return super().form_valid(form)  

class deletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
     model=models.Post
     select_related=('user','group')
     success_url=reverse_lazy('posts:all')

     def get_queryset(self):
          querySet=super().get_queryset() 
          return querySet.filter(user_id=self.request.user.id)
     def delete(self, *args,**kwargs):
           messages.success(self.request,"deleted")
          
           return super().delete( *args, **kwargs) 
    
        
        

    