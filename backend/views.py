from django.shortcuts import render
from rest_framework import viewsets, generics
from backend.models import Number, Pokemon
from backend.serializers.NumberSerializer import NumberSerializer
from backend.serializers.PokemonSerializer import PokemonSerializer
from django.http import JsonResponse

import random 
import string 


class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

    def get_queryset(self):
        queryset = Number.objects.all()
        number = self.request.query_params.get('number', None)
        letter = self.request.query_params.get('letter', None)
        if number is not None:
            queryset = queryset.filter(number=number)
        if letter is not None:
            queryset = queryset.filter(letter=letter)
        return queryset

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class =  PokemonSerializer

class CreateRandomNumber(generics.CreateAPIView):
    serializer_class = NumberSerializer

    def perform_create(self, serializer):

        random_number = random.randint(1,100)
        random_letter = random.choice(string.ascii_uppercase)

        serializer.save(number = random_number, letter = random_letter)


def random_pokemon_view(request):
    pokemons = list(Pokemon.objects.all())
    random_pokemons = random.sample(pokemons, 2) if len(pokemons) >= 2 else pokemons

    data = [{
        'nombre': pokemon.nombre,
        'numero_Pokedex': pokemon.numero_Pokedex,
        'tipo_primario': pokemon.tipo_primario,
        'tipo_secundario': pokemon.tipo_secundario or "N/A",
        'url_imagen': pokemon.url_imagen  # Incluir la URL de la imagen
    } for pokemon in random_pokemons]

    return JsonResponse(data, safe=False)