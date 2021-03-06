#-*- coding: utf-8 -*-
# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from django.contrib.csrf.middleware import csrf_exempt
#from django.shortcuts import get_object_or_404
#from django.core.mail import send_mail

from yonda.forms import *
from yonda.models import *
from yonda.tools import use_username_or_masuda

import solr
def index(request):
    """トップページ"""
    #loginしてるとき
    if request.method == "GET":
        return direct_to_template(request, "index.html", {"form":UrlPostForm()})
    if request.method == "POST":
        form = UrlPostForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('index'))
        user = use_username_or_masuda(request)
        Url.post_url(form.cleaned_data["url"], user)
        return HttpResponseRedirect(reverse('index'))

def login(request):
    """名前で登録する"""
    if request.method == "GET":
        return direct_to_template(request, 'login.html',{'form':LoginForm()})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('index'))
        if not User.objects.filter(name=form.cleaned_data["name"]).count():
            new_user = User(name=form.cleaned_data["name"])
            new_user.save()
        request.session['session_user'] = request.POST.get('name')
        return HttpResponseRedirect(reverse('index'))

def logout(request):
    """匿名に戻る"""
    if request.session.get('session_user'):
        del request.session['session_user']
    return HttpResponseRedirect(reverse('index'))

def timeline(request):
    """最近読んだURLのTimeline"""
    #とりあえず1000件取得する。ページングしない
    timeline = Url.objects.all().order_by('-atime')[:1000]
    return direct_to_template(request, "timeline.html",{'timeline':timeline})

def user_timeline(request, username):
    """ユーザーごとのTimeline"""
    #とりあえず1000件取得する。ページングしない
    user_timeline = Url.objects.filter(user=username).order_by('-atime')[:1000]
    username = use_username_or_masuda(request)
    return direct_to_template(request,"user_timeline.html", {"user_timeline":user_timeline, "username":username})

def feed(request, feed_id):
    """パーマリンクごとのURL"""
    feed= Url.objects.filter(pk=feed_id)
    users = Url.objects.filter(url=Url.objects.get(pk=feed_id))
    return direct_to_template(request,"feed.html", {"feed":feed, "users":users})

def bookmarklet(request):
    """ブックマークレット"""
    if request.method == "GET":
        title = request.GET.get('title')
        url = request.GET.get('url')
        user = use_username_or_masuda(request)
        return direct_to_template(request, 'bookmarklet.html',{'form': BookmalkletForm(initial={'title':title, 'user':user}), 'url':url})
    if request.method == "POST":
        form = BookmalkletForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse('bookmarklet'))
        user = form.cleaned_data["user"]
        Url.post_url(request.GET.get("url"), user, form.cleaned_data["title"])
        #一度bookmarklet_closeに誘導してからウィンドウを閉じる
        return direct_to_template(request, "bookmarklet_close.html",{})

def api(request):
    """APIについて"""
    return direct_to_template(request, "api.html", {})

def about(request):
    """おれについて"""
    return direct_to_template(request, "about.html", {})

@csrf_exempt
def post_api(request):
    """URLをポストするAPI。POSTのみ"""
    if request.method == "GET":
        raise
    user = request.POST.get("user")
    title = request.POST.get("title")
    url = request.POST.get("url")

    if not user:
        user = use_username_or_masuda(request)
    Url.post_url(url, user, title)
    return true

def url_count_api(request):
    """特定のURLに対して数を表示するAPI。GETのみ"""
    if not request.method == "GET":
        raise
    url = request.GET.get("url")
    count = Url.objects.filter(url=url).count()
    return HttpResponse(count)

def search(request):
    """検索。エゴサーチしたい"""
    if request.method == "GET":
        return direct_to_template(request, "search.html", {"form": SearchForm()})
    if request.method == "POST":
        form = SearchForm(request.POST)
        if not form.is_valid():
            return HttpResponseRedirect(reverse("search"))
        if not form.cleaned_data["title"]:
            if not form.cleaned_data["url"]:
                return HttpResponseRedirect(reverse("search"))
        s = solr.SolrConnection("http://localhost:8983/solr")
        #URLとTitleがある場合はtitleを優先する
        if form.cleaned_data["url"]:
            query_sring = "url:%s" % form.cleaned_data["url"]
        if form.cleaned_data["title"]:
            query_sring = "title:%s" % form.cleaned_data["title"]
        res = s.query(query_sring)
        return direct_to_template(request,"search.html", {"res":res, 'form':SearchForm()})
