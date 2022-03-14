from django.contrib import admin
from .models import Contact, Email

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
 
@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'coach_make', 'coach_model', 'coach_year')
