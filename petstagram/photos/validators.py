from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


def validate_file_size(image_object):
    if image_object.size > 1024 * 1024 * 5:  # image size of 5 MB
        raise ValidationError('The maximum file size that can be uploaded is 5MB')


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return max_size < file_size
