from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class RegistrationForm(UserCreationForm):
  email = forms.EmailField()
  bio = forms.CharField()

  class Meta:
    model = User
    fields=['username','email','bio', 'password1','password2']

  def __init__(self, *args,**kwargs):
      super(RegistrationForm,self).__init__(*args, **kwargs) 

      self.fields['username'].widget.attrs['class':'form-control']
      self.fields['email'].widget.attrs['class':'form-control'] 
      self.fields['password1'].widget.attrs['class':'form-control'] 
      self.fields['password2'].widget.attrs['class':'form-control']  

class EditProfile(UserChangeForm):
  email = forms.EmailField()
  bio = forms.CharField()

  class Meta:
    model = User
    fields=['username','email','bio']      
    