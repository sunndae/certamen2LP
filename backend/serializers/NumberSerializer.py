from rest_framework import serializers
from backend.models import Number

class NumberSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(required=False)
    letter = serializers.CharField(max_length=100, required=False)
    class Meta:
        model = Number
        fields = ['number', 'letter']  