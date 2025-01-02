from django.contrib import admin
from .models import Video, Comment


# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'status', 'upload_date')
    search_fields = ('title', 'description', 'author')
    ordering = ('-upload_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'upload_date')
    search_fields = ('text',)
    ordering = ('-upload_date',)