from datetime import datetime, timedelta

import pytest

from core.helpers import overlap_calculator
from core.tests.factories.campaign_factory import CampaignFactory
from core.tests.factories.product_factory import ProductFactory


@pytest.mark.django_db
def test_overlap_calculator_returns_overlap_value():
    """Assert an overlap value is returned"""
    product = ProductFactory()
    campaign_start_date = datetime.now()
    campaign_end_date = datetime.now() + timedelta(days=10)
    campaign = CampaignFactory(
        product=product, start_date=campaign_start_date, end_date=campaign_end_date
    )

    start_date = datetime.now() + timedelta(days=1)
    end_date = datetime.now() + timedelta(days=10)
    overlap = overlap_calculator(campaign, start_date, end_date)

    assert overlap > 0


@pytest.mark.django_db
def test_overlap_calculator_returns_no_overlap_value():
    """Assert dates do not overlap"""
    product = ProductFactory()
    campaign_start_date = datetime.now()
    campaign_end_date = datetime.now() + timedelta(days=10)
    campaign = CampaignFactory(
        product=product, start_date=campaign_start_date, end_date=campaign_end_date
    )

    start_date = datetime.now() + timedelta(days=11)
    end_date = datetime.now() + timedelta(days=12)
    overlap = overlap_calculator(campaign, start_date, end_date)

    assert overlap == 0


@pytest.mark.django_db
def test_overlap_calculator_value_for_the_same_dates():
    """Assert two dates with the same values returns and overlap"""
    product = ProductFactory()
    campaign_start_date = datetime.now()
    campaign_end_date = datetime.now() + timedelta(days=10)
    campaign = CampaignFactory(
        product=product, start_date=campaign_start_date, end_date=campaign_end_date
    )

    start_date = campaign_start_date
    end_date = campaign_end_date
    overlap = overlap_calculator(campaign, start_date, end_date)

    assert overlap > 0
