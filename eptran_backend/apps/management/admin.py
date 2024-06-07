from django.contrib.gis import admin
from apps.management.models import (
    User,
    Admin,
    Staff,
    Student,
    News,
    SavedNews,
    Game,
    GameStatistics,
)

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "is_superuser"]
    search_fields = ["name"]
    readonly_fields = ["updated_at", "created_at"]

admin.site.register(User, UserAdmin)

class AdminAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "permissions"]
    search_fields = ["user"]
    readonly_fields = ["updated_at", "created_at"]

admin.site.register(Admin, AdminAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "permissions"]
    search_fields = ["user"]
    readonly_fields = ["updated_at", "created_at"]

admin.site.register(Staff, StaffAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "permissions"]
    search_fields = ["user"]
    readonly_fields = ["updated_at", "created_at"]
    
admin.site.register(Student, StudentAdmin)

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