from django.urls import path # type: ignore
from pokemon import views
from . import views

urlpatterns = [
    path('index_pokemon', views.index_pok, name='index_pokemon'),
    path('pokemons_rest/', views.pokemons_rest, name='pokemons_rest'),
    path('add_pokemon/', views.add_pokemon, name='add_pokemon'),
]