#-*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup

import urllib2

def get_url_title(url):
    if "#!/" in url:
        url = url.replace("#!/","")
    try:
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        for s in soup('title'):
            souped_title = s.renderContents()
        title = souped_title.decode("utf-8")
    except:
        title = ""
    return title
