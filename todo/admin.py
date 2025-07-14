from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from todo.models import Task, CustomUser, Profile

admin.site.register([Task, Profile])

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name' ,'email', 'is_staff', 'is_superuser')

    add_fieldsets = (
        ('CreateUser', {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
