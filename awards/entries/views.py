from django.shortcuts import render,  get_object_or_404
from django.contrib.auth.decorators import login_required
from myusers.forms import RegistrationForm
from .forms import   UserProjectForm,CommentForm
from .models import Comment,Entry
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import  CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
  if request.method == 'POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form=RegistrationForm()    
  
  context={'form':form}
  return render(request,'auth/login.html', context)

# @login_required(login_url='/auth/login/')
def  userhome(request, **kwargs):
    posts =Entry.show_projects().order_by('-entry_date')
    
    return render(request, 'entries/home.html', {"posts":posts})

  


class AddComment(CreateView):
    model=Comment
    template_name='entries/addcomment.html'
    form_class=CommentForm
    def form_valid(self, form):
        form.instance.entry_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('landingpage')



class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'createpost.html'
    slug_field = "slug"
    fields =['userpic', 'title', 'description','livelink']
    

    form= UserProjectForm
    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def projectpost(self, request, *args, **kwargs):
        form = UserProjectForm(request.POST)
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context
    def get_success_url(self):
        return reverse('landingpage')






def LikeView(request, pk):
    project = get_object_or_404(Entry, id=request.POST.get('likeid'))
    project.likes.add(request.user)
    return HttpResponseRedirect(reverse('landingpage'), id=pk)