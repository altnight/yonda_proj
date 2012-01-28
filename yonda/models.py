#-*- coding:utf-8 -*-
from django.db import models

from BeautifulSoup import BeautifulSoup
import urllib2
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
    def post_url(cls, url):
        #import pdb;pdb.set_trace()
        if "#!/" in url:
            url = url.replace("#!/","")
        try:
            posted_user = request.session["session_user"]
        except:
            #TODO:増田
            posted_user = "増田"
        try:
            html = urllib2.urlopen(url).read()
            soup = BeautifulSoup(html)
            for s in soup('title'):
                souped_title = s.renderContents()
            decoded_title = souped_title.decode("utf-8")
            url_count = cls.objects.filter(url=url).filter(user=posted_user).count()
            url_count += 1
            url_instance = Url(url=url,
                               title=decoded_title,
                               user=posted_user,
                               count=url_count,
                               )
            url_instance.save()
        except:
            print 'error'
