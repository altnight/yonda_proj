#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(u"名前", max_length=255)
    email = models.CharField(u"email", max_length=255)
    password = models.CharField(max_length=255)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)
    atime = models.DateTimeField(u'更新日時',auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.email)

    class Meta:
        db_table = 'User'

class Url(models.Model):
    url = models.CharField(u"url", max_length=2048)
    title = models.CharField(u"title", max_length=2048)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)
    atime = models.DateTimeField(u'更新日時',auto_now=True, editable=False)
    #yonda = models.IntegerField(u"読んだ", default=0)

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = 'Url'
