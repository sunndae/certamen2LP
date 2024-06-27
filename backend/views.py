from django.shortcuts import render
from rest_framework import viewsets, generics
from backend.models import Number, Pokemon
from backend.serializers.NumberSerializer import NumberSerializer
from backend.serializers.PokemonSerializer import PokemonSerializer

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
