from django.contrib import admin

from petstagram.common.models import PhotoLike, PhotoComment


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    ordering = ('pet_photo', 'created_at', 'text')


@admin.register(PhotoLike)
class LikeAdmin(admin.ModelAdmin):
    pass
