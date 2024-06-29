from rest_framework import serializers
from backend.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=20)
    numero_pokedex = serializers.IntegerField(required=False)
    tipo_primario = serializers.CharField(max_length=100, required=False)
    tipo_secundario = serializers.CharField(max_length=100, required=False)
    url_imagen  = serializers.CharField(max_length=1000, required=False)

    class Meta:
        model = Pokemon
        fields = ['nombre', 'numero_Pokedex', 'tipo_primario', 'tipo_secundario', 'url_imagen']
