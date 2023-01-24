from django import forms
from .models import *

class userform(forms.Form):
    uname    = forms.CharField(max_length=20)
    email    = forms.CharField(max_length=20)
    psw = forms.CharField(max_length=20)