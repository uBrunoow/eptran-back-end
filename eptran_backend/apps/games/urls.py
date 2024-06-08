from apps.games import api
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"game", api.GameViewSet)
router.register(r"game-statistics", api.GameStatisticsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
