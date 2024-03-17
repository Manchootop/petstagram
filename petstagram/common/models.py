from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        Photo,
        on_delete=models.DO_NOTHING
    )
# photo_like = PhotoLike.objects \
#     .filter(pet_photo_id=pet_photo.pk, user=request.user)
