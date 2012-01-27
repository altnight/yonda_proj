#-*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup

import urllib2
import re

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

def deny_local_address(url):
    if re.match(r'https?://192\.168', url):
        raise
    if re.match(r'https?://127\.0', url):
        raise
