from django.contrib import admin

from petstagram.common.models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ('to_photo', 'date_time_of_publication', 'text')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
