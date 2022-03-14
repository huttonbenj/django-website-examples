from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Header Title', {
            'classes': ('wide',),
            'fields': ('section_title',),
        }),
        ('Your Contact Info', {
            'classes': ('wide',),
            'fields': ('address', 'phone', 'email'),
        }),

    )
