from apps.management import api
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", api.UserViewSet)
router.register(r"register-user", api.UserRegister, basename="register-user")
router.register(r"admin", api.AdminViewSet)
router.register(r"staff", api.StaffViewSet)
router.register(r"student", api.StudentViewSet)
router.register(r"news", api.NewsViewSet)
router.register(r"saved-news", api.SavedNewsViewSet)
router.register(r"game", api.GameViewSet)
router.register(r"game-statistics", api.GameStatisticsViewSet)

urlpatterns = [
    path("logout/", api.LogoutView.as_view()),
    path(
        "change_password/<uuid:pk>/",
        api.UserChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path("", include(router.urls)),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]