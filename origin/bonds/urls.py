from django.urls import include, path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import BondViewSet

router = routers.DefaultRouter()
router.register(r'bonds', BondViewSet, basename='Bond')

urlpatterns = [
    # Register the APIs
    path('', include(router.urls)),

    # Include a login for the APIs
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),

    # JSON JWT token URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
