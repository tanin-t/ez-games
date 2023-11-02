from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Player
        fields = ['id', 'name']
