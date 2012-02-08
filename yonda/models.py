#-*- coding:utf-8 -*-
from django.db import models

from yonda.tools import get_url_title, deny_local_address

# Create your models here.

class User(models.Model):
    name = models.CharField(u"name", max_length=128)
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
    count = models.IntegerField(u"回数", default=1)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)
    atime = models.DateTimeField(u'更新日時',auto_now=True, editable=False)

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = 'Url'

    @classmethod
    def post_url(cls, url, user, title=None):
        """URLをポストする共通メソッド"""
        deny_local_address(url)
        if not cls.objects.filter(url=url).filter(user=user).count():
            if not title:
                title = get_url_title(url)
            if not title:
                return
            url_instance = Url(url=url,
                               title=title,
                               user=user,
                               )
        else:
            url_instance = cls.objects.filter(url=url).get(user=user)
            url_instance.count += 1
        url_instance.save()
