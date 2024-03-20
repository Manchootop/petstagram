from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# def create_pet(request):
#     pet_form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect('details pet', username='lubo', pet_slug=created_pet.slug)
#     context = {
#         'pet_form': pet_form,
#     }
#
#     return render(request, 'pets/create_pet.html', context)

class PetCreateView(views.CreateView):
    model = Pet
    # fields = ['name', 'date_of_birth', 'personal_photo']
    template_name = 'pets/create_pet.html'
    form_class = PetCreateForm

    def get_success_url(self):
        return reverse('details pet', kwargs={
            'username': 'lubo',
            'pet_slug': self.object.slug
        })


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.filter(slug=pet_slug) \
        .get()

    pet_form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if pet_form.is_valid():
            pet_form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet,
    }

    return render(request, 'pets/edit_pet.html', context)


def details_pet(request, username, pet_slug):
    context = {
        'object': Pet.objects.get(slug=pet_slug)
    }

    return render(request, 'pets/details_pet.html', context)


class PetDetailView(views.DetailView):
    model = Pet     # or 'queryset'
    template_name = 'pets/details_pet.html'
    # slug_field = 'pet_slug'
    slug_url_kwarg = 'pet_slug'


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    pet_form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        pet_form.save()
        return redirect('index')

    context = {
        'pet_form': pet_form,
        'username': username,
        'pet': pet,
    }

    return render(request, 'pets/delete_pet.html', context)
