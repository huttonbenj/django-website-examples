from django.contrib.admin.decorators import register
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import GalleryPage, Image
from nested_admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
class ImageInline(NestedStackedInline):
    model = Image
    extra = 0

@register(GalleryPage)
class AboutPageAdmin(NestedModelAdmin):
    inlines = [ImageInline,]
    list_display = ('page_title',)