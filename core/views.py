from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.models import Campaign, Product
from core.serializers import CampaignSerializer, ProductSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    model = Campaign
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        "name": ["exact"],
        "product__name": ["exact"],
        "start_date": ["gte", "lte", "exact", "gt", "lt"],
        "end_date": ["gte", "lte", "exact", "gt", "lt"],
    }


class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]
