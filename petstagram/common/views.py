from django.shortcuts import render

from petstagram.photos.models import Photo


def index(request):
    context = {
        'pet_photos': Photo.objects.all(),
    }

    return render(request, 'common/index.html', context)