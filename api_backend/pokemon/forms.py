# forms.py
from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'type1', 'type2', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed']