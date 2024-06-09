from rest_framework import serializers
from .models import Game, GameStatistics
from django.db import transaction


class GameReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "name", "classification", "image", "link", "description", "created_at", "updated_at"]

class GameStatisticsReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameStatistics
        fields = ["id", "user", "game", "time_spent", "progress" , "fastest_time" , "created_at" , "updated_at"]