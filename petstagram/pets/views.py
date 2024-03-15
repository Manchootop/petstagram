from django.shortcuts import render

from petstagram.pets.models import Pet


def create_pet(request):
    context = {}

    return render(request, 'pets/create_pet.html')


def details_pet(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug)
    }

    return render(request, 'pets/details_pet.html', context)


def delete_pet(request, pk):
    context = {}

    return render(request, 'pets/delete_pet.html')


def edit_pet(request, pk):
    context = {}

    return render(request, 'pets/edit_pet.html')
