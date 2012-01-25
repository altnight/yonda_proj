#-*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from yonda.models import *

class UrlPostForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('url',)

class BookmalkletForm(forms.Form):
    title = forms.CharField(label=u"タイトル", required=True)
    url = forms.CharField(label=u"url", required=True, initial="http://")
    user= forms.CharField(label=u"名前", required=True, initial="増田")

#class SingupFrom(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('name','email')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)
