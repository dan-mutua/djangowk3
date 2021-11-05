from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class UserCreationView(generic.CreateView):
  form_class=UserCreationForm
  template_name='auth/register.html'
  success_url=reverse_lazy('login')
