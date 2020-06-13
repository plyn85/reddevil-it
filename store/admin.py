from django.contrib import admin
from .models import Product, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = (

        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('orderitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('transaction_id', 'date_ordered',
                       'full_name', 'total', 'grand_total',)

    fields = ("profile", 'transaction_id', 'date_ordered', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost', 'total', 'grand_total',
              )

    list_display = ('transaction_id', 'date_ordered', 'full_name', "profile", 'total', 'delivery_cost', 'grand_total',
                    )

    ordering = ('-date_ordered',)


admin.site.register(Order, OrderAdmin)
