from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.authentication import KeyTokenAuthentication
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (KeyTokenAuthentication,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
