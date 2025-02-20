from django.contrib import admin

from .models import *

# Registering models to make them manageable through the Django admin panel
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)