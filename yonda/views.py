#-*- coding: utf-8 -*-
# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.contrib.csrf.middleware import csrf_exempt
#from django.shortcuts import get_object_or_404
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
        
        url = form.cleaned_data["url"]
        Url.post_url(request, url)
        return HttpResponseRedirect(reverse('index'))

def login(request):
    if request.method == "GET":
        return direct_to_template(request, 'login.html',{'form':LoginForm()})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('index'))
        if not User.objects.filter(name=request.POST.get('name')).count():
            new_user = User(name=form.cleaned_data["name"])
            new_user.save()
        request.session['session_user'] = request.POST.get('name')
        return HttpResponseRedirect(reverse('index'))

def logout(request):
    if request.session.get('session_user'):
        del request.session['session_user']
    return HttpResponseRedirect(reverse('index'))

def timeline(request):
    timeline = Url.objects.all().order_by('-ctime')[:1000]
    return direct_to_template(request, "timeline.html",{'timeline':timeline})

def user_timeline(request, username):
    #user = User.objects.get(name=username)
    user_timeline = Url.objects.filter(user=username).order_by('-ctime')[:1000]
    return direct_to_template(request,"user_timeline.html", {"user_timeline":user_timeline})

def feed(request, feed_id):
    feed= Url.objects.filter(pk=feed_id)
    return direct_to_template(request,"feed.html", {"feed":feed})

def bookmarklet(request):
    if request.method == "GET":
        #クエリからtitleとurlをとってくる
        title = request.GET.get('title')
        url = request.GET.get('url')
        if request.session.get("session_user"):
            user = request.session["session_user"]
        else:
            #TODO:増田
            user = "増田"
        #bookmarkletなのでinitialをつける
        return direct_to_template(request, 'bookmarklet.html',{'form': BookmalkletForm(initial={'title':title, 'user':user}), 'url':url})
    if request.method == "POST":
        form = BookmalkletForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('bookmarklet'))

        if request.session.get("session_user"):
            user = request.session["session_user"]
        else:
            #TODO:増田
            user = request.POST.get("user")
        Url.post_url(request, request.GET.get("url"), form.cleaned_data["title"], user)
        return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def post_api(request):
    if request.method == "GET":
        raise
    user = request.POST.get("user")
    title = request.POST.get("title")
    url = request.POST.get("url")
    if not user:
        user = "増田"
    Url.post_url(request, url, title, user)
    return true
