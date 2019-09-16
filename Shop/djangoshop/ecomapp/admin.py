from django.contrib import admin
from ecomapp.models import Category, Brand, Product, CartItem, Cart, Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'address',
                    'buying_types', 'date', 'comments', 'status']

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)