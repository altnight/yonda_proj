#-*- encoding: utf-8 -*-
#from django.forms import ModelForm
from django import forms

import re
#from yonda.models import *

class UrlPostForm(forms.Form):
    url = forms.CharField(label=u"URL", required=True, initial="http://",
                          widget=forms.TextInput(attrs={"class":"url_postform"}))
    def clean_url(self):
        url = self.cleaned_data['url']
        if not re.match(r'^https?://', url):
            raise forms.ValidationError(u'httpかhttpsで初めてください')
        if re.match(r'^https?://192\.168', url):
            raise forms.ValidationError(u'プライベートアドレスはどうよ')
        if re.match(r'^https?://127\.0', url):
            raise forms.ValidationError(u'プライベートアドレスはどうよ')
        return url

class BookmalkletForm(forms.Form):
    title = forms.CharField(label=u"タイトル", required=True,
                          widget=forms.TextInput(attrs={"class":"title_postform"}))
    #url = forms.CharField(label=u"url", required=True, initial="http://",
    #                      widget=forms.TextInput(attrs={"class":"url_postform"}))
    user= forms.CharField(label=u"名前", required=True, initial="増田",
                          widget=forms.TextInput(attrs={"class":"name_postform"}))
     

class LoginForm(forms.Form):
    name = forms.CharField(label=u"名前", required=True, initial="増田",
                          widget=forms.TextInput(attrs={"class":"name_postform"}))

class SearchForm(forms.Form):
    title = forms.CharField(label=u"タイトルで検索する", required=False,
                          widget=forms.TextInput(attrs={"class":"title_postform"}))
    url = forms.CharField(label=u"URLで検索する", required=False,
                          widget=forms.TextInput(attrs={"class":"url_postform"}))
