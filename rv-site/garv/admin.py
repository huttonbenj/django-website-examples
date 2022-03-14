from django.contrib import admin
from .models import Garv

# Register your models here.
@admin.register(Garv)
class GarvAdmin(admin.ModelAdmin):
    pass

