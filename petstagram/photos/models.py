from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size, MaxFileSizeValidator

SIZE_5_MB = 5 * 1024 * 1024


class Photo(models.Model):
    photo = models.ImageField(
        validators=(
            MaxFileSizeValidator(limit_value=SIZE_5_MB),
        ),
        upload_to='pet_photos/',
        blank=False,
        null=False,
    )  # custom validator for files > 5MB
    description = models.TextField(

        max_length=300,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

    @property
    def photo_count(self):
        return self.photolike_set.count()