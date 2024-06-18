from rest_framework import serializers # type: ignore

from pokemon.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'type1', 'type2', 'hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed']