from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser, UserProfile


class CustomUserAdmin(UserAdmin):
    # add_form  Both when you want to add custom fields
    # form
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)