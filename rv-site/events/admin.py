from django.contrib import admin
from .models import Event, Seo, PageTitle
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class PageTitleSingleInline(NestedStackedInline):
    model = PageTitle
    extra = 1
    max_num = 1
    verbose_name = 'Page Title'
    verbose_name_plural = 'Page Title'


class SeoSingleInline(NestedStackedInline):
    model = Seo
    extra = 1
    max_num = 1
    exclude = ['page_title', 'main_page']


class SeoMainInline(NestedStackedInline):
    model = Seo
    extra = 1
    max_num = 1
    exclude = ['main_page', 'event']


@admin.register(Event)
class EventAdmin(NestedModelAdmin):
    inlines = [PageTitleSingleInline, SeoSingleInline]
    list_display = ('short_title', 'background_image', 'datetime')
    fieldsets = (
        ('Event', {
            'fields': (
                ('event_type', 'short_title', 'background_image', 'datetime', 'location', 'description')
            ),
        }),
    )

@admin.register(PageTitle)
class PageTitleAdmin(NestedModelAdmin):
    inlines = [SeoMainInline, ]
    exclude = ['event', ]
    list_display = ('title', 'description', 'background_image')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(seo__main_page='event_feed')

