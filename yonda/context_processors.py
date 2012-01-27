#-*- coding: utf-8 -*-
from django.conf import settings
from django.core.cache import cache
from django.utils.encoding import force_unicode, DjangoUnicodeDecodeError

def domain(request):
    return {'DOMAIN':settings.DOMAIN}

