from django.contrib import admin
from backend.models import Number
from backend.models import Pokemon
# Register your models here.


class NumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'letter') # campos a mostrar
    search_fields = ('number', 'letter')

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_Pokedex', 'tipo_primario')
    search_fields = ('nombre', 'numero_Pokedex')


admin.site.register(Number, NumberAdmin)
admin.site.register(Pokemon, PokemonAdmin)

