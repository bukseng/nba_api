from rest_framework import serializers

from .models import Stat


class StatSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source="player.name")
    class Meta:
        model = Stat
        fields = ["id", "player_name", "year"]
    