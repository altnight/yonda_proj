from yonda.models import *
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'ctime', )
    readonly_fields = ('ctime', )

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'user', 'ctime',)
    readonly_fields = ('ctime',)

admin.site.register(User, UserAdmin)
admin.site.register(Url, UrlAdmin)

