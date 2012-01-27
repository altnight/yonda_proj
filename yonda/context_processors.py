#-*- coding: utf-8 -*-
from django.conf import settings
from django.core.cache import cache
from django.utils.encoding import force_unicode, DjangoUnicodeDecodeError

from yonda.models import User
def display_user(request):
    user = ''
    if "session_user" in request.session:
        user = User.objects.get(name=request.session.get("session_user"))
    return {"display_user": user}

def domain(request):
    return {'DOMAIN':settings.DOMAIN}

