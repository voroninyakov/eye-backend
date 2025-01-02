from django.contrib import admin

from .models import EUser, Profile


# Register your models here

@admin.register(EUser)
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser')

@admin.register(Profile)
class AdminUser(admin.ModelAdmin):
    list_display = ('user', 'name')