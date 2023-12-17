from django.contrib import admin
from django.db import connection

from .models import *


@admin.register(Counters)
class CountersAdmin(admin.ModelAdmin):
    list_display = ('users_counter', 'classrooms_counter')


@admin.register(AuthGroup)
class AuthGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(AuthorizationUserGroups)
class AuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'group_id')

