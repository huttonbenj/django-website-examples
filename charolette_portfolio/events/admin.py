from django.contrib import admin
from .models import Events, Images

# Register your models here.
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        events = Events.objects.all()
        if change == True:
            for i in events:
                i.header_title = obj.header_title
                i.background_image = obj.background_image  
                i.save()

        if change == False:
            for i in events:
                i.header_title = obj.header_title
                i.background_image = obj.background_image
                i.save()



        return super(EventsAdmin, self).save_model(request, obj, form, change)

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass