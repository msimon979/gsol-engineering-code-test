from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import Campaign, Product, User


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
