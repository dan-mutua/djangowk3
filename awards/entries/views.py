from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Entry

# Create your views here.
class HomeView(ListView):
  model= Entry
  template_name='entries/home.html'
  context_object_name= "blog_entries"
  ordering= ['-entry_date']

class EntryView(DetailView):
  model = Entry
  template_name= 'entries/entry_detail.html'  

class CreateEntry(CreateView):
  model = Entry
  template_name= 'entries/create_entry.html'  
  fields=['entry_tittle','entry_text']

  def form_valid(self,form):
    form.instance.entry_author = self.request.user
    return super().form_valid(form)