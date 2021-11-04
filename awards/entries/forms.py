from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entry, UserProfile


#This will create the news letter
class RegistrationForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields=['username','email', 'password1','password2']






class UserProfileUpdateForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ['userpic','user', 'email', 'phonenumber', 'bio', 'gender']


class UserProjectForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields = ['userpic','title', 'description', 'livelink']