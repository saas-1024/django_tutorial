from django.contrib import admin
from django.db.models import Count

from spot_deals.models.spot_deals import SpotDeal
from spot_deals.models.spot_deals import CryptoAsset


@admin.register(CryptoAsset)
class CryptoAssetAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'ticker')

    def count_assets(self, obj):
        return obj.CryptoAsset.count()  # bad practice to count like this

    # autocomplete_fields = ['full_name',]
    search_fields = ('full_name',)
    # def get_queryset(self, request):
    #     queryset = admin.CryptoAsset.objects.annotate(
    #         assets_count=Count('cryptoasset__id')
    #     )


@admin.register(SpotDeal)
class SpotDealAdmin(admin.ModelAdmin):
    list_display = ('date_deal', 'usd_amount', 'exchange')
    autocomplete_fields = ['asset_deal', ]

