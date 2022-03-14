from django.contrib import admin
from .models import Cart, CartBackground

# Register your models here.
# @admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartBackground)
class CartBackgroundAdmin(admin.ModelAdmin):
    pass