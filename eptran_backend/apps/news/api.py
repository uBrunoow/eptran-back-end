from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import BlacklistedToken, OutstandingToken
from rest_framework.response import Response
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
from .models import ( News, SavedNews)
from .serializers import (
    NewsReadOnlySerializer,
    SavedNewsReadOnlySerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsReadOnlySerializer

class SavedNewsViewSet(viewsets.ModelViewSet):
    queryset = SavedNews.objects.all()
    serializer_class = SavedNewsReadOnlySerializer