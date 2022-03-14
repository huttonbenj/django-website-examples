from django.contrib import admin
from .models import Intro, Rule, WarningMessage, Seo

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display = ('small_title', 'large_title', 'description')


@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    exclude = ('main_page',)

admin.site.register(Rule)
admin.site.register(WarningMessage)
