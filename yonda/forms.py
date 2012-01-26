#-*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from yonda.models import *

class UrlPostForm(forms.Form):
    url = forms.CharField(label=u"url", required=True, initial="http://",
                          widget=forms.TextInput(attrs={"class":"url_postform"}))

class BookmalkletForm(forms.Form):
    title = forms.CharField(label=u"タイトル", required=True,
                          widget=forms.TextInput(attrs={"class":"title_postform"}))
    url = forms.CharField(label=u"url", required=True, initial="http://",
                          widget=forms.TextInput(attrs={"class":"url_postform"}))
    user= forms.CharField(label=u"名前", required=True, initial="増田",
                          widget=forms.TextInput(attrs={"class":"name_postform"}))

#class SingupFrom(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('name','email')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)
