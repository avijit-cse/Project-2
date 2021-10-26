from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from App_Login.models import userprofile


class CreateNewUser(UserCreationForm):
    email=forms.EmailField(label='',required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'placeholder':'username'}))
    password1=forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(label='',required=True,widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model= User
        fields=('email','username','password1','password2')


class Editprofile(forms.ModelForm):
    dob=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=userprofile
        exclude=('user',)