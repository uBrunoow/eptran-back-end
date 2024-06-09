from rest_framework import (
    generics,
    mixins,
    permissions,
    response,
    status,
    views,
    viewsets,
)
from utils.actions import DRFAction
from .models import ( GameStatistics, Game)
from .serializers import (
    GameReadOnlySerializer,
    GameStatisticsReadOnlySerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameReadOnlySerializer

class GameStatisticsViewSet(viewsets.ModelViewSet):
    queryset = GameStatistics.objects.all()
    serializer_class = GameStatisticsReadOnlySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["user", "game"]
