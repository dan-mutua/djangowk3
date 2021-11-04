from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entry, UserProfile,Comment


#This will create the news letter
class RegistrationForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields=['username','email', 'password1','password2']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('name','body')

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'})
        }


class UserProfileUpdateForm(forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ['userpic','user', 'email', 'phonenumber', 'bio', 'gender']


class UserProjectForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields = ['userpic','title', 'description', 'livelink']