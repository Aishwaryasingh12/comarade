from django import forms

from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.Form,forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    firstname= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pref= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    dob= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

