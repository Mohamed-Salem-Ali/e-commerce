from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
class CustomUserAdmin(UserAdmin):
    model=Customer
    list_display = ('username', 'email', 'phone_number', 'address', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'address')}),
    )

admin.site.register(Customer, CustomUserAdmin)