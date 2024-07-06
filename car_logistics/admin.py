from datetime import datetime
from django.contrib import admin
from .models import Lot, Customer, Company, Warehouse, Account, Auction
from django.contrib import messages


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ['auto', 'vin', 'lot', 'customer', 'status', 'get_wait_days', 'date_purchase', 'payment_date', 'date_warehouse',
                    'date_booking', 'data_container', 'date_unloaded', 'account', 'auction', 'company', 'price', 'keys']
    # list_filter = ['wait']
    search_fields = ['vin', 'auto', 'lot', 'customer__name']  # Добавляем 'customer__name' для поиска по имени клиента
    readonly_fields = ['status_changed']
    list_editable = ['status']
    list_display_links = ['auto', 'vin', 'lot']
    date_hierarchy = 'status_changed'
    fieldsets = (
        (None, {
            'fields': ('auto', 'vin', 'lot', 'account', 'auction', 'customer', 'company', 'price')
        }),
        ('Dates', {
            'fields': (
                'date_purchase', 'payment_date', 'date_warehouse', 'date_booking', 'data_container', 'date_unloaded')
        }),
        ('Photos', {
            'fields': ('bos', 'photo_a', 'keys', 'photo_d', 'photo_w')
        }),
        ('Warehouse', {
            'fields': ('warehouse', 'status')
        }),
    )
    # filter_horizontal = ['customer']
    # raw_id_fields = ['company']
    autocomplete_fields = ['warehouse', 'company']
    radio_fields = {'status': admin.HORIZONTAL}
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if obj.account.customer != obj.customer:
            messages.error(request, "Account and customer do not match. Are you sure?")
        super().save_model(request, obj, form, change)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_accounts']

    def display_accounts(self, obj):
        return ", ".join([account.name for account in obj.accounts.all()])

    display_accounts.short_description = 'Accounts'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer']
    search_fields = ['name']


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
