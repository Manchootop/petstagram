from django.shortcuts import render

from petstagram.photos.models import Photo


def create_photo(request):
    context = {}

    return render(request, 'photos/create_photo.html')


def details_photo(request, pk):
    context = {
        'pet_photo': Photo.objects.get(pk=pk)
    }
    return render(request, 'photos/details_photo.html', context)


def edit_photo(request, pet_hpk):
    context = {}
    return render(request, 'photos/edit_photo.html', context)
