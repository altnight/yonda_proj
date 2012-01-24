from yonda.models import *
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'ctime', 'atime', 'is_active',)
    readonly_fields = ('ctime', 'password', )

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'user', 'ctime',)
    readonly_fields = ('ctime',)

admin.site.register(User, UserAdmin)
admin.site.register(Url, UrlAdmin)

