from django.contrib.gis import admin
from django.contrib.auth.hashers import make_password
from apps.games.models import (
    Game,
    GameStatistics,
)

class GameAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "classification"]
    search_fields = ["name"]
    readonly_fields = ["updated_at", "created_at"]

admin.site.register(Game, GameAdmin)

class GameStatisticsAdmin(admin.ModelAdmin):
    list_display = ["id", "game", "user"]
    search_fields = ["game"]
    readonly_fields = ["updated_at", "created_at"]

admin.site.register(GameStatistics, GameStatisticsAdmin)