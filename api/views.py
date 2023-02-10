from rest_framework import viewsets
# Create your views here.

from core.models import Campaign, Product
from api.serializers import CampaignSerializer, ProductSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    model = Campaign
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()