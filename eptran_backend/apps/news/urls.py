from apps.news import api
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"news", api.NewsViewSet)
router.register(r"saved-news", api.SavedNewsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
