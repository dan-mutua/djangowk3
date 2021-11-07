from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy


from entries.models import Profile

# Create your views here.
class UserCreationView(generic.CreateView):
  form_class=UserCreationForm
  template_name='auth/register.html'
  success_url=reverse_lazy('login')


class UserEdit(generic.UpdateView):
  form_class=UserChangeForm
  template_name='auth/edit_profile.html'
  success_url=reverse_lazy('home')

  def get_object(self):
    return self.request.user


class ShowProfilePageView(DetailView):
    model=Profile
    template_name='auth/profileview.html'

    def get_context_data(self, *args, **kwargs):
      users=Profile.objects.all()
      context=super(ShowProfilePageView, self).get_context_data(*args,**kwargs)

      page_user=get_object_or_404(Profile,id=self.kwargs['pk'])

      context["page_user"]=page_user
      return context

