from django.db import models

# Create your models here.

class Number(models.Model):
    number = models.IntegerField()
    letter = models.CharField()

    