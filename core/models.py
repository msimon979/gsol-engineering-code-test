"""
An extremely contrived example of Outcome Health business objects.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User of the application. Consider them internal only for the sake of the exercise.
    """


class Product(models.Model):
    """
    This could be a drug or a supplement.
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    """
    An advertisement campaign. This is how we make our money.
    """

    name = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_active_campaign(product):
        return Campaign.objects.filter(product=product).first()
