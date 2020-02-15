from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):

    list_display = ('username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
