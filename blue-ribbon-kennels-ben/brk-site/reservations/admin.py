from django.contrib import admin
from django.template.response import TemplateResponse
from django.conf.urls import url
from .models import Kennel, Reservation
from payments.models import Product
from datetime import datetime, timedelta
from collections import OrderedDict

@admin.register(Kennel)
class KennelAdmin(admin.ModelAdmin):
    list_display = ('number', 'booked',)
    search_fields = ('number',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('kennel', 'type', 'email', 'first_name', 'last_name', 'dogs_name', 'status')
    fields = (
        'kennel', 
        'type', 
        'start_date', 
        'end_date', 
        'number_of_days', 
        'extended_stay', 
        'pickup_date', 
        'additional_cost', 
        'cost', 
        'overall_cost',
        'first_name',
        'last_name',
        'email',
        'phone',
        'street',
        'city',
        'state',
        'postal_code',
        'dogs_name',
        'dogs_breed',
        'dogs_sex',
        'dogs_age',
        'shot_records',
        'comments',
        'status',
        )
    search_fields = ['first_name', 'last_name', 'email', 'status', 'dogs_name', 'type', 'kennel__number']

    class Media:
        js = ('js/jquery.js', 'admin/js/dynamic_fields.js',)



    def get_form(self, request, obj=None, **kwargs):
        form = super(ReservationAdmin, self).get_form(request, obj, **kwargs)
        return form

    def get_urls(self):
        urls = super(ReservationAdmin, self).get_urls()
        my_urls = [
            url(r'^kennel_map/$', self.my_view),
            url(r'^monthly_summary/$', self.monthly_summary),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           kennels=Kennel.objects.all().order_by('number'),
           reservations=Reservation.objects.all(),
        )
        return TemplateResponse(request, "admin/kennel_map.html", context)    

    def monthly_summary(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/monthly-summary.html", context)    

    def save_model(self, request, obj, form, change):
        if obj.extended_stay == False:
            obj.pickup_date = None 
            obj.additional_cost = None 
            obj.start_date_additional = None
            obj.end_date_additional = None
        if not obj.id:
            price = obj.overall_cost or obj.cost
            obj.payment = Product(name=obj.type, customer_email=obj.email, price=price, amount=obj.number_of_days)
            obj.payment.save()
            obj.kennel.booked = True
            obj.kennel.save()
        super(ReservationAdmin, self).save_model(request, obj, form, change)