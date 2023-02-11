from datetime import datetime

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.tests.factories.campaign_factory import CampaignFactory
from core.tests.factories.product_factory import ProductFactory


@pytest.mark.django_db
class CampaignViewSetTests(APITestCase):
    def test_get_campaigns(self):
        """Assert pagination campaigns are returned"""
        product = ProductFactory()
        for _ in range(11):
            CampaignFactory(
                product=product, start_date=datetime.now(), end_date=datetime.now()
            )

        url = reverse("campaigns-list")
        response = self.client.get(url)
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        # Total pagination count
        assert data["count"] == 11
        assert len(data["results"]) == 10

    def test_get_campaigns_with_filters(self):
        """Assert filtering campaigns returns correct data"""
        product = ProductFactory()
        CampaignFactory(
            product=product, start_date=datetime.now(), end_date=datetime.now()
        )
        campaign_name = CampaignFactory(
            product=product, start_date=datetime.now(), end_date=datetime.now()
        )

        url = (
            reverse("campaigns-list")
            + f"?name={campaign_name.name}&product__name={product.name}"
        )
        response = self.client.get(url)
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        # Total pagination count
        assert data["count"] == 1
        assert data["results"][0]["name"] == campaign_name.name
        assert data["results"][0]["product"]["name"] == product.name

    def test_post_campaign(self):
        """Assert posting a new campaign is successful"""
        product = ProductFactory()
        url = reverse("campaigns-list")
        payload = {
            "product": {"id": product.id},
            "name": "test",
            "start_date": "2023-01-01",
            "end_date": "2023-01-02",
        }
        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["name"] == "test"
        assert data["start_date"] == "2023-01-01"
        assert data["end_date"] == "2023-01-02"
        assert data["product"]["id"] == product.id

    def test_post_campaign_deactivates_old_campaign(self):
        """Assert posting a new campaign is successful and deactivates the previous one"""
        product = ProductFactory()
        campaign = CampaignFactory(
            product=product, start_date="2023-01-01", end_date="2023-01-02"
        )
        assert campaign.is_active is True

        url = reverse("campaigns-list")
        payload = {
            "product": {"id": product.id},
            "name": "test",
            "start_date": "2023-01-03",
            "end_date": "2023-01-04",
        }
        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["name"] == "test"
        assert data["start_date"] == "2023-01-03"
        assert data["end_date"] == "2023-01-04"
        assert data["product"]["id"] == product.id
        assert data["is_active"] is True

        campaign.refresh_from_db()
        assert campaign.is_active is False

    def test_post_campaign_deactivates_old_campaign(self):
        """Assert posting a new campaign fails due to date overlap"""
        product = ProductFactory()
        campaign = CampaignFactory(
            product=product, start_date="2023-01-01", end_date="2023-01-05"
        )
        assert campaign.is_active is True

        url = reverse("campaigns-list")
        payload = {
            "product": {"id": product.id},
            "name": "test",
            "start_date": "2023-01-03",
            "end_date": "2023-01-04",
        }
        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            "non_field_errors": [
                f"Campaign test overlaps with campaign {campaign.name}"
            ]
        }

        campaign.refresh_from_db()
        assert campaign.is_active is True


@pytest.mark.django_db
class ProductViewSetTests(APITestCase):
    def test_get_products(self):
        """Assert pagination products are returned"""
        for _ in range(11):
            ProductFactory()

        url = reverse("products-list")
        response = self.client.get(url)
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        # Total pagination count
        assert data["count"] == 11
        assert len(data["results"]) == 10

    def test_get_products_by_name(self):
        """Assert filtering products returns correct data"""
        ProductFactory()
        product = ProductFactory()

        url = reverse("products-list") + f"?name={product.name}"
        response = self.client.get(url)
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        # Total pagination count
        assert data["count"] == 1
        assert data["results"][0]["name"] == product.name
