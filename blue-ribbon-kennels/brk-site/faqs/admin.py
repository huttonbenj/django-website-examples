from django.contrib import admin
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import FaqPage, AccordionEntry
from nested_admin import NestedStackedInline, NestedModelAdmin

class AccordianEntryInline(NestedStackedInline):
    model = AccordionEntry
    extra = 0

@admin.register(FaqPage)
class AboutPageAdmin(NestedModelAdmin):
    inlines = [AccordianEntryInline,]
    list_display = ('page_title',)