from django.contrib import admin
from .models import FacilityPage, Image
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from nested_admin import NestedStackedInline, NestedModelAdmin

class ImageInline(NestedStackedInline):
    model = Image
    extra = 0

@admin.register(FacilityPage)
class FacilityPageAdmin(NestedModelAdmin):
    inlines = [ImageInline,]
    list_display = ('page_title', 'content_title')