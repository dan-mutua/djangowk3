
  
from django.db.models.base import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from myusers.forms import RegistrationForm
from .forms import     UserProfileUpdateForm, UserProjectForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Comment,Entry
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import  CreateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def register(request):
  if request.method == 'POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
  else:
    form=RegistrationForm()    
  
  context={'form':form}
  return render(request,'entries/register.html', context)

@login_required(login_url='/entries/login/')
def  userhome(request, **kwargs):
    posts =Entry.show_projects().order_by('-entry_date')
    
    return render(request, 'entries/home.html', {"posts":posts})

  
def UserProfile(request):
    profileform = UserProfileUpdateForm(instance=request.user.userprofile)
    if request.method == 'POST':
        profileform=UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if profileform.is_valid():
            profileform.save(commit=False)

            return redirect('cloneapp:profile')

        else:
            profileform = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user': request.user,
        'profileform': profileform
    }
    return render(request, 'profile.html', context)

@login_required
def EditProfile(request):
    profileform = UserProfileUpdateForm(instance=request.user.userprofile)
    pform = None
    if request.method == 'POST':
        profileform=UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if profileform.is_valid():
            pform=profileform.save(commit=False)
            pform.user = request.user
            pform.profile = profileform
            pform.save()


            return redirect('profile')

        else:
            profileform = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user': request.user,
        'profileform': profileform, 
        'pform':pform,
    }
    return render(request, 'profileedit.html', context)

class AddComment(CreateView):
    model=Comment
    template_name='entries/addcomment.html'
    fields='__all__'
    



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
        return reverse('index')






def LikeView(request, pk):
    project = get_object_or_404(Entry, id=request.POST.get('likeid'))
    project.likes.add(request.user)
    return HttpResponseRedirect(reverse('index'), id=pk)