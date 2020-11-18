from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Bond
from .serializers import BondReadSerializer, BondWriteSerializer


class AuthMixin:
    authentication_classes = (SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated,)


class BondViewSet(AuthMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows bonds to be viewed or edited
    """
    filterset_fields = ['legal_name']

    def get_queryset(self):
        """
        Return the list of bonds for the currently authenticated user
        """
        user = self.request.user
        return Bond.objects.filter(user=user)

    def get_serializer_class(self, *args, **kwargs):
        serializer_class = BondReadSerializer
        if self.request.method in ['PATCH', 'POST', 'PUT']:
            serializer_class = BondWriteSerializer

        return serializer_class
