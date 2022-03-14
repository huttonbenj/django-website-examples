from django.contrib import admin
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import AboutPage, AboutTab, AboutAccordian, TeamMember
# from sorl.thumbnail import get_thumbnail
from nested_admin import NestedStackedInline, NestedModelAdmin

class TeamMemberInline(NestedStackedInline):
    model = TeamMember
    extra = 0

class AboutAccordianInline(NestedStackedInline):
    model = AboutAccordian
    extra = 0

class AboutTabInline(NestedStackedInline):
    model = AboutTab
    extra = 0

@admin.register(AboutPage)
class AboutPageAdmin(NestedModelAdmin):
    inlines = [AboutTabInline, AboutAccordianInline, TeamMemberInline]
    list_display = ('page_title',)
    # def save_model(self, request, obj, form, change):
    #     print(change)
    #     # im = get_thumbnail(obj.page_title_image, '1600', crop='smart', quality=100)
    #     # obj.page_title_image = f"/{'/'.join(im.url.split('/')[2:])}"
    #     super().save_model(request, obj, form, change)