from django.contrib import admin
import nested_admin
from .models import Package, Rate, Detail, PageTitle, Seo
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class DetailInline(nested_admin.NestedStackedInline):
    model = Detail
    extra = 0


class RateInline(nested_admin.NestedStackedInline):
    model = Rate
    extra = 0
    inlines = [DetailInline]


@admin.register(Package)
class PackageAdmin(nested_admin.NestedModelAdmin):
    inlines = [ RateInline ]
    ordering = ('name',)
    list_display = ('name', 'description')
    fieldsets = (
        ('Package', {
            'fields': (
                ('name', )
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
