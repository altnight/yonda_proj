#-*- coding: utf-8 -*-
from yonda.models import User

from django.conf import settings
from django.core.cache import cache
from django.utils.encoding import force_unicode, DjangoUnicodeDecodeError

def user_session(request):
    user = ''
    if 'session_user' in request.session:
        #user = User.objects.get(id=request.session['session_user'].id)
        user = User.objects.get(name=request.session.get('session_user'))
    return {
        'display_user': user,
    }
def domain(request):
    return settings.DOMAIN
