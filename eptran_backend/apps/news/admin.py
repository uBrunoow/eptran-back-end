from django.contrib.gis import admin
from django.contrib.auth.hashers import make_password
from apps.news.models import (
    News,
    SavedNews,
)

class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title"]
    search_fields = ["title"]
    readonly_fields = ["updated_at", "created_at"]

admin.site.register(News, NewsAdmin)

class SavedNewsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "news"]
    search_fields = ["news"]
    readonly_fields = ["updated_at", "created_at"]

admin.site.register(SavedNews, SavedNewsAdmin)