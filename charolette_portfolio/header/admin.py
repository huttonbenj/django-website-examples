from django.contrib import admin
from .models import Header
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline

# Register your models here.
@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Display', {
            'classes': ('wide',),
            'fields': ('display',),
        }),
        ('Navigation', {
            'classes': ('wide',),
            'fields': ('navlogo',),
        }),
        ('Background', {
            'classes': ('wide',),
            'fields': ('bg',),
        }),
        ('Text', {
            'classes': ('wide',),
            'fields': ('intro', 'name'),
        }),
        ('Style', {
            'classes': ('wide',),
            'fields': ('style', 'logo'),
        }),
    )
