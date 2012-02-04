from yonda.models import *
from django.contrib import admin

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'user', 'ctime',)
    readonly_fields = ('ctime',)

admin.site.register(Url, UrlAdmin)

