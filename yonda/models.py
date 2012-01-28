#-*- coding:utf-8 -*-
from django.db import models

from yonda.tools import get_url_title

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

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = 'Url'

    @classmethod
    def post_url(cls, request, url):
        #import pdb;pdb.set_trace()
        if request.session.get("session_user"):
            posted_user = request.session["session_user"]
        else:
            #TODO:増田
            posted_user = "増田"
        title = get_url_title(url)
        url_count = cls.objects.filter(url=url).filter(user=posted_user).count()
        url_count += 1
        url_instance = Url(url=url,
                           title=title,
                           user=posted_user,
                           count=url_count,
                           )
        url_instance.save()
