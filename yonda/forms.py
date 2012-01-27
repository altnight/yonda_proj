#-*- encoding: utf-8 -*-
#from django.forms import ModelForm
from django import forms

import re
#from yonda.models import *

class UrlPostForm(forms.Form):
    url = forms.CharField(label=u"url", required=True, initial="http://",
                          widget=forms.TextInput(attrs={"class":"url_postform"}))
    def clean_url(self):
        url = self.cleaned_data['url']
        if not re.match(r'^https?://', url):
            raise forms.ValidationError(u'httpかhttpsで初めてください')
        return url

class BookmalkletForm(forms.Form):
    title = forms.CharField(label=u"タイトル", required=True,
                          widget=forms.TextInput(attrs={"class":"title_postform"}))
    #url = forms.CharField(label=u"url", required=True, initial="http://",
    #                      widget=forms.TextInput(attrs={"class":"url_postform"}))
    user= forms.CharField(label=u"名前", required=True, initial="増田",
                          widget=forms.TextInput(attrs={"class":"name_postform"}))
     
    def clean_url(self):
        url = self.cleaned_data['url']
        if not re.match(r'^https?://', url):
            raise forms.ValidationError(u'httpかhttpsで初めてください')
        return url

class LoginForm(forms.Form):
    name = forms.CharField(label=u"名前", required=True, initial="増田",
                          widget=forms.TextInput(attrs={"class":"name_postform"}))
