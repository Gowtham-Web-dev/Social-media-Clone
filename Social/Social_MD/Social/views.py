from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Social.forms import UserCreateForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def custom_logout(request):
    logout(request)
    # Redirect to a different URL after logout
    return HttpResponseRedirect(reverse('thank'))  # Replace 'home' with the URL name of your choice


# Create your views here.

class Sidnup(CreateView):
    form_class=UserCreateForm
    success_url=reverse_lazy('login')
    template_name='account/signup.html'