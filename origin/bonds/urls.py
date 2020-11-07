from django.urls import include, path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import BondViewSet

router = routers.DefaultRouter()
router.register(r'bonds', BondViewSet)

urlpatterns = [
    # Register the APIs
    path('', include(router.urls)),

    # JSON JWT token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
