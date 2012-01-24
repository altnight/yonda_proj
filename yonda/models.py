#-*- coding:utf-8 -*-
from django.db import models

from BeautifulSoup import BeautifulSoup
import urllib2
# Create your models here.

class User(models.Model):
    name = models.CharField(u"名前", max_length=255)
    email = models.CharField(u"email", max_length=255)
    password = models.CharField(max_length=255)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)
    atime = models.DateTimeField(u'更新日時',auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'User'

class Url(models.Model):
    url = models.CharField(u"url", max_length=2048)
    title = models.CharField(u"title", max_length=2048)
    #user = models.ForeignKey(User, verbose_name=u'ユーザー')
    user = models.CharField(u"ユーザー", max_length=255, editable=False)
    ctime = models.DateTimeField(u'登録日時',auto_now_add=True, editable=False)
    atime = models.DateTimeField(u'更新日時',auto_now=True, editable=False)
    #yonda = models.IntegerField(u"読んだ", default=0)

    def __unicode__(self):
        return self.url

    class Meta:
        db_table = 'Url'

    @classmethod
    def post_url(cls, url):
        if "#!/" in url:
            url = url.replace("#!/","")
        #try:
        #    posted_user = User.objects.get(name=request.session["session_user"])
        #except:
        #    #TODO:増田
        #    posted_user = User.objects.get(pk=2)
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
            url_instance = Url(url=form.cleaned_data["url"],
                               title=decoded_title,
                               user=posted_user
                               )
            url_instance.save()
        except:
            print 'error'
