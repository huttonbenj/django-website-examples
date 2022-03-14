from django.contrib import admin
from .models import LotForSale, PageTitle, Seo, OwnerForms
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class SeoMainInline(NestedStackedInline):
    model = Seo
    extra = 1
    max_num = 1
    exclude = ['main_page',]

@admin.register(PageTitle)
class PageTitleAdmin(NestedModelAdmin):
    inlines = [SeoMainInline, ]
    list_display = ('title', 'description', 'background_image')

admin.site.register(OwnerForms)
