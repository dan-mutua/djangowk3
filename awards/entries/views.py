
  
from django.db.models.base import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, NewsLetterForm, CommentsForm,  UserProfileUpdateForm, UserProjectForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView,UpdateView, CreateView, DeleteView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def landing(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect("home.html")
        messages.error(request, "Unsuccessful registration. Invalid Information")
    form = SignUpForm()
    return render(request, 'entries/home.html', context={"signup_form":form})


@login_required(login_url='/emaillogin/')
def  userhome(request, **kwargs):
    posts =Entry.show_projects().order_by('-pub_date')
    # id = int(request.POST.get('projectid'))
    likey= get_object_or_404(Entry)
    totallikes= likey.totallikes()
    # alllikes = likey.likes.filter(id = id)
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        c_form = CommentsForm(request.POST)
        if form.is_valid() and c_form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['email']
            recipient = Subscriber(name=name, email=email)
            recipient.save()
            # -------------------------
            comment=c_form.cleaned_data['comment']
            c_form.save()
            HttpResponseRedirect('userhome')
    else:
        form =NewsLetterForm()
        c_form = CommentsForm(request.POST)
    return render(request, 'entries/home.html', {"posts":posts, "NLform":form, 'form':c_form, 'totallikes':totallikes})

  
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
class FindProjectView(DetailView):
    model = Entry
    template_name = 'projectfound.html'
    slug_field = "slug"

    form = CommentsForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def project(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            project = self.get_object()
            form.instance.user = request.user
            form.instance.project = project
            form.save()

            return redirect(reverse('project', kwargs={"form":form, 'slug':project.slug}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context
    
    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(comment=self.object.id).count()
        post_comments = Comment.objects.all().filter(comment=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })
        return context
    




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
        c_form = CommentsForm(request.POST)
        if form.is_valid() and c_form.is_valid():
            project = self.get_object()
            form.instance.user = request.user
            form.instance.project = project
            form.save()

            return redirect(reverse("project", kwargs={"projectform":form,"cform":c_form, 'pk':project.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context
    def get_success_url(self):
        return reverse('index')

class DeleteProject(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name='delete.html'
    success_url = reverse_lazy('index')


    def get_queryset(self):
        
        return Entry.objects.all()


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentsForm
    template_name = 'addcomment.html'


def CommentPost(request, pk):
    project = get_object_or_404(Entry)
    comments = project.comments.filter(id = pk)
    comment = None

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.user = request.user
            comment.project = project
            comment.save()
            return redirect('index')

    else:
        form = CommentsForm()
    return render(request, 'addcomment.html', {'comments':comment, 'comments': comments, 'form':form, 'project':project, 'id':pk})

def LikeView(request, pk):
    project = get_object_or_404(Entry, id=request.POST.get('likeid'))
    project.likes.add(request.user)
    return HttpResponseRedirect(reverse('index'), id=pk)