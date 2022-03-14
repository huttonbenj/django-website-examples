from django.contrib import admin
from nested_admin import NestedStackedInline, NestedModelAdmin

# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Slide, Testimonial, TestimonialSection
from services.models import Service

@admin.register(Slide)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'button_text', 'button_link')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'slot_position')


class TestimonialInline(NestedStackedInline):
    model = Testimonial
    extra = 0

@admin.register(TestimonialSection)
class TestimonialSectionAdmin(NestedModelAdmin):
    inlines = [TestimonialInline,]
    list_display = ('title', 'background_image')
   