from django.contrib import admin
from jazzmin.utils import order_with_respect_to
from .models import Header, Slider, Slide, Intro, Overview, About, Footer, Testimonials, Testimonial, Packages, PackageItem
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Register your models here.
@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('logo_white', 'logo_colors')

@admin.register(Intro)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_one', 'image_two')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'position_slot')

@admin.register(Overview)
class OverviewAdmin(admin.ModelAdmin):
    list_display = ('title_large', 'position_slot')

class PackageItemInline(admin.StackedInline):
    model = PackageItem
    extra = 0

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    inlines = [ PackageItemInline, ]
    list_display = ('name',)
    fieldsets = (
        ('Package', {
            'fields': (
                ('name',)
            ),
        }),
    )

class SlideInline(admin.StackedInline):
    model = Slide
    extra = 0
    list_display = ('background_image', 'title_large', 'title_small', 'description', 'description_span', 'button_1_label', 'button_2_label', 'order_slot')

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    inlines = [ SlideInline, ]
    class Media:
        js = ('admin/js/custom-admin.js',)    

class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 0

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    inlines = [ TestimonialInline, ]
    fieldsets = (
        ('Section Background Image', {
            'fields': (
                ('background_image',)
            ),
        }),
    )

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('logo', )
