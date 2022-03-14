from django.contrib import admin, messages
from django.contrib.admin import AdminSite
from django.db import models
from django.urls import path
from django.template.response import TemplateResponse

from polymorphic.formsets import polymorphic_modelformset_factory, PolymorphicFormSetChild
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline

from .models import SectionTitleDescription, Slideshow, Service, Services, ContactUs, Header, AboutUs, TypedText, SectionTitle, SocialMedia, Image, Portfolio


admin.site.site_title = "Henderson Construction"
admin.site.site_header = "Henderson Construction"
admin.site.index_title = "Welcome to your Admin Dashboard"

class PortfolioChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Portfolio  


@admin.register(SectionTitleDescription)
class SectionTitleDescriptionAdmin(PortfolioChildAdmin):
    base_model = SectionTitleDescription
    list_display = ['title', 'description']
    def save_model(self, request, obj, form, change):
        p = SectionTitleDescription.objects.all()
        all_main = [s.id for s in p]
        save = True

        if len(all_main) >= 1 and not obj.id in all_main:
            messages.set_level(request, messages.ERROR)
            messages.error(
                request, "You can only have 1 Title and 1 Description, your last entry was NOT saved")
            save = False

        if save == True:
            super(SectionTitleDescriptionAdmin, self).save_model(
                request, obj, form, change)

@admin.register(Image)
class ImageAdmin(PortfolioChildAdmin):
    base_model = Image  
 
    fieldsets = (
        ('Image', {
            'fields': ('photo', 'category', 'slot_number', 'description'),

        }),
    )
    list_display = ['photo', 'category', 'slot_number', 'description']

    def save_model(self, request, obj, form, change):
        images = Image.objects.all()
        all_slots = [s for s in images]
        slots = [str(s.slot_number)
                 for s in images if not str(s.slot_number) == 'None']
        slots_match = [
            s.__dict__ for s in all_slots if str(s.id) == str(obj.id)]
        slots_objs = [('image', str(obj.photo)), ('slot_number', str(obj.slot_number))]
        save = True

        if change == False:
            if len(all_slots) >= 10:
                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You can only have 10 Normal Portfolio images, your last entry was NOT saved")
                save = False

            if str(obj.slot_number) in slots:
                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "Slot numbers must be unique, your last entry was NOT saved")
                save = False

        if change == True:
            if len(slots_match) < 1:
                save = True

            if len(slots_match) > 0:
                slots_match = {str(s): str(slots_match[0][s]) for s in slots_match[0] if not s ==
                               '_state' and not s == 'id' and not s == 'description' and not s == 'status'}
                change = [s for s in slots_objs if not s[1] == slots_match['photo'] and not s[1] == slots_match['slot_number']]
                duplicate = [s for s in change if s[0]
                             == 'slot_number' and s[1] in slots]

                if not duplicate == []:
                    messages.set_level(request, messages.ERROR)
                    messages.error(
                        request, "Slot numbers must be unique, your last entry was NOT saved")
                    save = False

        if save == True:
            obj.category = obj.category.lower()
            rem_space = str(obj.category).split()
            obj.cat_link = str(''.join(rem_space))
        
            rem_sym = [s for s in obj.cat_link if not s == '/' and not s == ' ']        
            obj.cat_link = str(''.join(rem_sym))
           
            super(ImageAdmin, self).save_model(
                request, obj, form, change)

@admin.register(Slideshow)
class SlideshowAdmin(PortfolioChildAdmin):
    base_model = Slideshow
    list_display = ['slide_photo', 'category']
    def save_model(self, request, obj, form, change):
        slides = Slideshow.objects.all()
        cat = str(obj.category)
        for i in slides:
            i.category = cat
            i.save()

        super(SlideshowAdmin, self).save_model(
            request, obj, form, change)

@admin.register(Portfolio)
class PortfolioParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """

    base_model = Portfolio  
    child_models = (SectionTitleDescription, Image, Slideshow)
    list_filter = (PolymorphicChildModelFilter,) 
    polymorphic_list = True


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        social = SocialMedia.objects.all()
        save = True

        if change == False:
            if len(social) >= 1 and not obj.id == social[0].id:

                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You can only have one Social Media Object, your last entry was NOT saved")
                save = False

        if save == True:
            super(SocialMediaAdmin, self).save_model(
                request, obj, form, change)


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        header = Header.objects.all()
        save = True 
        
        if change == False:
            if len(header) >= 1 and not obj.id == header[0].id:
           
                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You can only have one Header page, your last entry was NOT saved")
                save = False

        if save == True:
            super(HeaderAdmin, self).save_model(
                request, obj, form, change)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        about = AboutUs.objects.all()
        save = True 
        
        if change == False:
            if len(about) >= 1 and not obj.id == about[0].id:
           
                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You can only have one About Us page, your last entry was NOT saved")
                save = False

        if save == True:
            super(AboutUsAdmin, self).save_model(
                request, obj, form, change)


@admin.register(TypedText)
class TypedTextAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        typed_text = TypedText.objects.all()
        save = True

        if change == False:
            if len(typed_text) >= 1 and not obj.id == typed_text[0].id:

                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You can only have one Typed Text Section page, your last entry was NOT saved")
                save = False

        if save == True:
            super(TypedTextAdmin, self).save_model(
                request, obj, form, change)


@admin.register(Service)
class ServiceAdmin(PortfolioChildAdmin):
    base_model = Service
    def save_model(self, request, obj, form, change):
        service = Service.objects.all()
        services = [str(s.title) for s in service]
        save = True

        if change == False:
            if len(service) == 12:
                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You can only have 12 Services on the Home Page your last entry was NOT saved")
                save = False                 

            match = [s for s in service if obj.id == s.id]
            if len(match) > 0:
                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You have already created this service, your last entry was NOT saved")
                save = False    

        if save == True:
            super(ServiceAdmin, self).save_model(
                request, obj, form, change)


@admin.register(SectionTitle)
class SectionTitleAdmin(PortfolioChildAdmin):
    base_model = SectionTitle
    def save_model(self, request, obj, form, change):
        save = True 
        service = SectionTitle.objects.all()

        if change == False:
            if len(service) >= 1 and not obj.id == service[0].id:

                messages.set_level(request, messages.ERROR)
                messages.error(
                    request, "You can only have one Main Title for the Services page, your last entry was NOT saved")
                save = False

        if save == True:
            super(SectionTitleAdmin, self).save_model(
                request, obj, form, change)


@admin.register(Services)
class ServicesParentAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Services  # Optional, explicitly set here.
    child_models = (SectionTitle, Service)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        c = ContactUs.objects.all()
        all_main = [s.id for s in c]
        save = True

        if len(all_main) >= 1 and not obj.id in all_main:
            messages.set_level(request, messages.ERROR)
            messages.error(
                request, "You can only 1 Title and 1 Description, your last entry was NOT saved")
            save = False

        if save == True:
            super(ContactUsAdmin, self).save_model(
                request, obj, form, change)



