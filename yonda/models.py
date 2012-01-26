#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(u"名前", max_length=255)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'User'

class Url(models.Model):
    url = models.CharField(u"url", max_length=2048)
    title = models.CharField(u"title", max_length=2048)
    #user = models.ForeignKey(User, verbose_name=u'ユーザー')
    user = models.CharField(u"ユーザー", max_length=255)
    count = models.IntegerField(u"回数", default=0)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)
    #yonda = models.IntegerField(u"読んだ", default=0)

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = 'Url'
