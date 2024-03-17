from django.urls import path, include
from . import views as views

urlpatterns = [
    path('add/', views.create_pet, name='create pet'),
    path('', views.create_pet, name='create pet'),
    # path(include('<str:username>/pet/<slug:pet slug>/')),
        path('<str:username>/pet/<slug:pet_slug>/',
         include([
             path('', views.details_pet, name='details pet'),
             path('edit/', views.edit_pet, name='edit pet'),
             path('delete/', views.delete_pet, name='delete pet'),
                ]),
         ),
]
