from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'customer_name', 'total_cost', 'amount_paid', 'amount_owed', 'has_paid', 'paid_in_full')
    fields = ('name', 'customer_email', 'customer_name', 'stripe_payment_intent', 'price', 'amount', 'total_cost', 'amount_paid', 'amount_owed', 'has_paid', 'paid_in_full',)
    search_fields = ['customer_email', 'customer_name']
    