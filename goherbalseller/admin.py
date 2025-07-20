from django.contrib import admin
from .models import SellerProfile, SellerPayout

@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'is_approved', 'commission_rate', 'created_at')
    list_filter = ('is_approved', 'commission_rate')
    search_fields = ('business_name', 'user__username', 'user__email')
    readonly_fields = ('created_at',)

@admin.register(SellerPayout)
class SellerPayoutAdmin(admin.ModelAdmin):
    list_display = ('seller', 'net_amount', 'status', 'period_start', 'period_end', 'requested_at')
    list_filter = ('status', 'requested_at', 'processed_at')
    search_fields = ('seller__username', 'transaction_id')
    readonly_fields = ('requested_at',)