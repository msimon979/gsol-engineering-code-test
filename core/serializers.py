from django.core.exceptions import ValidationError
from rest_framework import serializers

from core.helpers import overlap_calculator
from core.models import Campaign, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=256, required=False)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
        )


class CampaignSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()

    class Meta:
        model = Campaign
        fields = ("id", "name", "product", "start_date", "end_date", "is_active")

    def campaign_overlap(self, attrs):
        """Check if the validated data overlaps with an existing campaign"""
        product = attrs["product"]
        start_date = attrs["start_date"]
        end_date = attrs["end_date"]

        # If there is an active campaign check for date overlaps
        if latest_campaign := Campaign.get_active_campaign(product):
            overlap_count = overlap_calculator(latest_campaign, start_date, end_date)
            if overlap_count > 0:
                return latest_campaign.name

        return None

    def validate(self, attrs):
        """Custom validations for overlapping campaigns"""
        if overlap_campaign := self.campaign_overlap(attrs):
            raise ValidationError(
                f"Campaign {attrs['name']} overlaps with campaign {overlap_campaign}"
            )

        if attrs["start_date"] >= attrs["end_date"]:
            raise ValidationError(f"Start date is greater than end date")
        return attrs

    def validate_product(self, value):
        """Ensure product exists"""
        try:
            product = Product.objects.get(id=value["id"])
        except Product.DoesNotExist:
            raise ValidationError(f"Product id {value['id']} does not exist")

        return product

    def create(self, validated_data):
        product = validated_data.pop("product")

        # If a campaign existed before this in activate it
        if active_campaign := Campaign.get_active_campaign(product):
            active_campaign.is_active = False
            active_campaign.save()

        campaign = Campaign.objects.create(product=product, **validated_data)

        return campaign
