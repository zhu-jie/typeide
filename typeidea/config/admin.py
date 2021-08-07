from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Link, SideBar
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site
# Register your models here.

@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

@admin.register(LogEntry)
class  LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']