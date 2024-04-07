from django.urls import path

from .jwt_views import CustomRefreshView
from .views import (
    RegisterView,
    LoginView,
    UserDetailsView,
    ReferalsView
)


urlpatterns = [
    path("register/", RegisterView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("my-details/", UserDetailsView.as_view(), name="my_details"),
    path("my-referals/", ReferalsView.as_view(), name="my_referals"),
    path("refresh/", CustomRefreshView.as_view(), name="refresh"),
]
