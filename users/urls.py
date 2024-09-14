from django.urls import path
from users import views
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.UserCreateAPIView.as_view(), name="user-create"),
    path("list/", views.UserListAPIView.as_view(), name="user-list"),
    path(
        "users/<int:pk>/retrieve/",
        views.UserRetrieveAPIView.as_view(),
        name="user-retrieve",
    ),
    path(
        "users/<int:pk>/update/", views.UserUpdateAPIView.as_view(), name="user-update"
    ),
    path(
        "users/<int:pk>/destroy/",
        views.UserDestroyAPIView.as_view(),
        name="user-destroy",
    ),
]
