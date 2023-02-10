from rest_framework import serializers

from core.models import Campaign, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=256, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name',)


class CampaignSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()

    class Meta:
        model = Campaign
        fields = ('name', 'product', 'start_date', 'end_date')

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product = Product.objects.get(id=product_data['id'])
        campaign = Campaign.objects.create(product=product, **validated_data)

        return campaign