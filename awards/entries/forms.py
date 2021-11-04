from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entry, Entry, Subscriber , Comment, UserProfile


#This will create the news letter
class RegistrationForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields=['username','email', 'password1','password2']
    
class NewsLetterForm(forms.ModelForm):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')
    class Meta:
        model=Subscriber
        fields=("your_name", "email",)


class CommentsForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':'4', 'placeholder': 'enter your comment'}))
    class Meta:
        model=Comment
        fields= ['user', 'comment']

class UserProfileUpdateForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ['userpic','user', 'email', 'phonenumber', 'bio', 'gender']


class UserProjectForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields = ['userpic','title', 'description', 'livelink']