from django.contrib import admin
from .models import Lot, Image, Features, PageTitle, Seo
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from ownership.models import LotForSale

class ImageInline(NestedStackedInline):
    model = Image
    extra = 0


class FeaturesInline(NestedStackedInline):
    model = Features
    extra = 0


class LotForSaleInline(NestedStackedInline):
    model = LotForSale
    extra = 1
    max_num = 1

@admin.register(Lot)
class LotAdmin(NestedModelAdmin):
    inlines = [ImageInline, FeaturesInline, LotForSaleInline]
    ordering = ('number',)
    list_display = ('number', 'package', )
    fieldsets = (
        ('General Details', {
            'fields': (
                ('number', 'description', 'package', )
            ),
        }),
    )

class SeoMainInline(NestedStackedInline):
    model = Seo
    extra = 1
    max_num = 1
    exclude = ['main_page',]


@admin.register(PageTitle)
class PageTitleAdmin(NestedModelAdmin):
    inlines = [SeoMainInline, ]
    list_display = ('title', 'description', 'background_image')
 
