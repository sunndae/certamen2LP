from django.db import models

# Create your models here.

class Number(models.Model):
    number = models.IntegerField()
    letter = models.CharField()

    
class Pokemon(models.Model):
    nombre = models.CharField(max_length=20)
    numero_Pokedex = models.IntegerField()
    tipo_primario = models.CharField(max_length=15)
    tipo_secundario = models.CharField(max_length=15, null=True, blank=True)
    url_imagen = models.CharField(max_length = 1000)