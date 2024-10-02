from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.views import UserViewSet
from dj_rest_auth.views import LoginView

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("", include(router.urls)),
]
