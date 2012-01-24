#-*- coding: utf-8 -*-
# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
#from django.core.mail import send_mail

from yonda.forms import *
from yonda.models import *

def index(request):
    #loginしてるとき
    if request.method == "GET":
        return direct_to_template(request, "index.html", {"form":UrlPostForm()})
    if request.method == "POST":
        form = UrlPostForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('index'))
        url_instance = Url(url=form.cleaned_data["url"])
        url_instance.save()
        return HttpResponseRedirect(reverse('index'))

def signup(request):
    if request.method == "GET":
        return direct_to_template(request, 'signup.html',{'form':SingupFrom()})
    if request.method == "POST":
        form = SingupFrom(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('index'))
        #存在しないユーザーならindexに戻す
        #if not User.objects.filter(name=request.POST.get('name')).count():
        #    return HttpResponseRedirect(reverse('index'))
        new_user = User(name=form.cleaned_data["name"], 
                        email=form.cleaned_data["email"])
        new_user.save()
        request.session['session_user'] = request.POST.get('name')
        return HttpResponseRedirect(reverse('index'))

def login(request):
    if request.method == "GET":
        return direct_to_template(request, 'login.html',{'form':LoginForm()})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('index'))
        #存在しないユーザーならindexに戻す
        if not User.objects.filter(name=request.POST.get('name')).count():
            return HttpResponseRedirect(reverse('index'))
        request.session['session_user'] = request.POST.get('name')
        return HttpResponseRedirect(reverse('index'))

def logout(request):
    if request.session.get('session_user'):
        del request.session['session_user']
    return HttpResponseRedirect(reverse('index'))
