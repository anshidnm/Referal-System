from rest_framework_simplejwt.views import TokenRefreshView

from .schemas import Documentation


@Documentation.REFRESH
class CustomRefreshView(TokenRefreshView):
    pass