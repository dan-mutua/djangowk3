from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Entry

# Create your views here.
class HomeView(ListView):
  model= Entry
  template_name='entries/home.html'
  context_object_name= "blog_entries"

class EntryView(DetailView):
  model = Entry
  template_name= 'entries/entry_detail.html'  

class CreateEntry(CreateView):
  model = Entry
  template_name= 'entries/create_entry.html'  
  fields=['entry_title','entry_text']