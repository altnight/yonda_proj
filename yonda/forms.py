#-*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from yonda.models import *

class UrlPostForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('url',)

#class SingupFrom(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('name','email')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)
