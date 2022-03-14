from django.contrib import admin
from django import forms
from jazzmin.utils import order_with_respect_to
from .models import Blog, Categories
from .models import Seo, PageTitle

from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class CategoriesInline(NestedStackedInline):
    model = Categories
    extra = 1


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
    exclude = ['blog', 'main_page']


@admin.register(Blog)
class BlogAdmin(NestedModelAdmin):
    inlines = [CategoriesInline, PageTitleSingleInline, SeoSingleInline]
    list_display = ('title', 'image', 'datetime')
    fieldsets = (
        ('Blog Post', {
            'fields': (
                ('user', 'title', 'image', 'story', 'datetime')
            ),
        }),
    )


@admin.register(PageTitle)
class PageTitleAdmin(NestedModelAdmin):
    inlines = [SeoMainInline, ]
    exclude = ['blog', ]
    list_display = ('title', 'description', 'background_image')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(seo__main_page='blog_feed')


