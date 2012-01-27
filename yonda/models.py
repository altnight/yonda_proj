#-*- coding:utf-8 -*-
from django.db import models

from yonda.tools import get_url_title

import re
# Create your models here.

class User(models.Model):
    name = models.CharField(u"名前", max_length=255)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'User'

class Url(models.Model):
    url = models.CharField(u"url", max_length=1024)
    title = models.CharField(u"title", max_length=1024)
    #user = models.ForeignKey(User, verbose_name=u'ユーザー')
    user = models.CharField(u"ユーザー", max_length=128)
    count = models.IntegerField(u"回数", default=0)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = 'Url'

    @classmethod
    def post_url(cls, request, url, title=None, post_user=None):
        if not post_user:
            if request.session.get("session_user"):
                post_user = request.session["session_user"]
            else:
                #TODO:増田
                post_user = "増田"
        if not title:
            title = get_url_title(url)
        if not title:
            return
        if re.match(r'https?://192\.168', url):
            return
        if re.match(r'https?://127\.0', url):
            return
        url_count = cls.objects.filter(url=url).filter(user=post_user).count()
        url_count += 1
        url_instance = Url(url=url,
                           title=title,
                           user=post_user,
                           count=url_count,
                           )
        url_instance.save()
