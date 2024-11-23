from django.contrib import admin
from .models import Topic, Comment, Reply

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__karimov')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'created_at')
    search_fields = ('content', 'user__karimov')
    list_filter = ('created_at',)

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'created_at')
    search_fields = ('content', 'user__karimov')
    list_filter = ('created_at',)
