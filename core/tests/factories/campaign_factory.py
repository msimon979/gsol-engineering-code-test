import factory

from core.models import Campaign


class CampaignFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Campaign

    name = factory.Faker("name")
