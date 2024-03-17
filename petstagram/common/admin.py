from django.contrib import admin

from petstagram.common.models import Comment, PhotoLike


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ('to_photo', 'date_time_of_publication', 'text')


@admin.register(PhotoLike)
class LikeAdmin(admin.ModelAdmin):
    pass
