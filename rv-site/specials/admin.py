from django.contrib import admin
from .models import Seo, PageTitle, Special
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')


class SeoMainInline(NestedStackedInline):
    model = Seo
    extra = 1
    max_num = 1
    exclude = ['main_page',]


@admin.register(PageTitle)
class PageTitleAdmin(NestedModelAdmin):
    inlines = [SeoMainInline, ]
    list_display = ('title', 'description', 'background_image')
