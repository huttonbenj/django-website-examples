from django.contrib import admin
from .models import Artwork

# # Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):

    fieldsets = (
        ('All Gallery Images', {
            'classes': ('wide', 'collapse'),
            'fields': ('image', 'image_title', 'image_description','image_category', 'image_sub_category', 'framed_unframed', 'price'),
        }),
        ('Home Page Gallery', {
            'classes': ('wide', 'collapse'),
            'fields': ('gallery_header', 'gallery_title', 'gallery_style', 'gallery_columns','number_of_photos'),
        }),
        ('Artwork Main Page Header', {
            'classes': ('wide', 'collapse'),
            'fields': ('artwork_header_title', 'artwork_header_image', 'artwork_gallery_style', 'artwork_gallery_columns'),
        }),
        ('Originals Page Header', {
            'classes': ('wide', 'collapse'),
            'fields': ('originals_header_title', 'originals_header_image', 'originals_gallery_style', 'originals_gallery_columns'),
        }),
        ('Oil Page Header', {
            'classes': ('wide', 'collapse'),
            'fields': ('oils_header_title', 'oils_header_image', 'oils_gallery_style', 'oils_gallery_columns'),
        }),
        ('Watercolor Page Header', {
            'classes': ('wide', 'collapse'),
            'fields': ('watercolor_header_title', 'watercolor_header_image', 'watercolor_gallery_style', 'watercolor_gallery_columns'),
        }),
        ('Prints Page Header', {
            'classes': ('wide', 'collapse'),
            'fields': ('prints_header_title', 'prints_header_image', 'prints_gallery_style', 'prints_gallery_columns'),
        }),
        ('Framed Page Header', {
            'classes': ('wide', 'collapse'),
            'fields': ('framed_header_title', 'framed_header_image', 'framed_gallery_style', 'framed_gallery_columns'),
        }),
        ('Unframed Page Header', {
            'classes': ('wide', 'collapse'),
            'fields': ('unframed_header_title', 'unframed_header_image', 'unframed_gallery_style', 'unframed_gallery_columns'),
        }),
    )

    # def render_change_form(self, request, context, *args, **kwargs):
    #     # here we define a custom template
    #     self.change_form_template = 'admin/artwork/change_fieldset.html'
    #     extra = {
    #         'help_text': "This is a help message. Good luck filling out the form."
    #     }

    #     context.update(extra)
    #     return super(ArtworkAdmin, self).render_change_form(request, context, *args, **kwargs)
    first = Artwork.objects.all()
    if len(first) > 0:
        def add_view(self, request, form_url='', extra_context=None):
            last = Artwork.objects.all()
               
            g = request.GET.copy()
            g.update({
                'artwork_header_image': last[0].artwork_header_image,
                'originals_header_image': last[0].originals_header_image,
                'oils_header_image': last[0].oils_header_image,
                'watercolor_header_image': last[0].watercolor_header_image,
                'prints_header_image': last[0].prints_header_image,
                'framed_header_image': last[0].prints_header_image,
                'unframed_header_image': last[0].prints_header_image,
        
            })

            request.GET = g

            return super(ArtworkAdmin, self).add_view(request, form_url, extra_context)
    

    def save_model(self, request, obj, form, change):
        artwork = Artwork.objects.all()
        if change == True:
            for i in artwork:
                i.gallery_header = obj.gallery_header
                i.gallery_style = obj.gallery_style
                i.gallery_columns = obj.gallery_columns
                i.number_of_photos = obj.number_of_photos

                i.artwork_gallery_style = obj.artwork_gallery_style
                i.artwork_gallery_columns = obj.artwork_gallery_columns
                i.artwork_header_title = obj.artwork_header_title
                i.artwork_header_image = obj.artwork_header_image

                i.originals_gallery_style = obj.originals_gallery_style
                i.originals_gallery_columns = obj.originals_gallery_columns
                i.originals_header_title = obj.originals_header_title
                i.originals_header_image = obj.originals_header_image

                i.oils_gallery_style = obj.oils_gallery_style
                i.oils_gallery_columns = obj.oils_gallery_columns
                i.oils_header_title = obj.oils_header_title
                i.oils_header_image = obj.oils_header_image

                i.watercolor_gallery_style = obj.watercolor_gallery_style
                i.watercolor_gallery_columns = obj.watercolor_gallery_columns
                i.watercolor_header_title = obj.watercolor_header_title
                i.watercolor_header_image = obj.watercolor_header_image

                i.prints_gallery_style = obj.prints_gallery_style
                i.prints_gallery_columns = obj.prints_gallery_columns
                i.prints_header_title = obj.prints_header_title
                i.prints_header_image = obj.prints_header_image

                i.framed_gallery_style = obj.framed_gallery_style
                i.framed_gallery_columns = obj.framed_gallery_columns
                i.framed_header_title = obj.framed_header_title
                i.framed_header_image = obj.framed_header_image

                i.unframed_gallery_style = obj.unframed_gallery_style
                i.unframed_gallery_columns = obj.unframed_gallery_columns
                i.unframed_header_title = obj.unframed_header_title
                i.unframed_header_image = obj.unframed_header_image
                i.save()
            
        if change == False:
            for i in artwork:
                i.gallery_header = obj.gallery_header
                i.gallery_style = obj.gallery_style
                i.gallery_columns = obj.gallery_columns
                i.number_of_photos = obj.number_of_photos

                i.artwork_gallery_style = obj.artwork_gallery_style
                i.artwork_gallery_columns = obj.artwork_gallery_columns
                i.artwork_header_title = obj.artwork_header_title
                i.artwork_header_image = obj.artwork_header_image

                i.originals_gallery_style = obj.originals_gallery_style
                i.originals_gallery_columns = obj.originals_gallery_columns
                i.originals_header_title = obj.originals_header_title
                i.originals_header_image = obj.originals_header_image

                i.oils_gallery_style = obj.oils_gallery_style
                i.oils_gallery_columns = obj.oils_gallery_columns
                i.oils_header_title = obj.oils_header_title
                i.oils_header_image = obj.oils_header_image

                i.watercolor_gallery_style = obj.watercolor_gallery_style
                i.watercolor_gallery_columns = obj.watercolor_gallery_columns
                i.watercolor_header_title = obj.watercolor_header_title
                i.watercolor_header_image = obj.watercolor_header_image

                i.prints_gallery_style = obj.prints_gallery_style
                i.prints_gallery_columns = obj.prints_gallery_columns
                i.prints_header_title = obj.prints_header_title
                i.prints_header_image = obj.prints_header_image

                i.framed_gallery_style = obj.framed_gallery_style
                i.framed_gallery_columns = obj.framed_gallery_columns
                i.framed_header_title = obj.framed_header_title
                i.framed_header_image = obj.framed_header_image

                i.unframed_gallery_style = obj.unframed_gallery_style
                i.unframed_gallery_columns = obj.unframed_gallery_columns
                i.unframed_header_title = obj.unframed_header_title
                i.unframed_header_image = obj.unframed_header_image
                i.save()

        # for i in range(4):

        #     Artwork.objects.create(header_title=obj.header_title,
        #                    header_image=obj.header_image,
        #                    image_title=obj.image_title,
        #                    image_category=obj.image_category,
        #                    image=obj.image,
        #                    portfolio_style=obj.portfolio_style)


        return super(ArtworkAdmin, self).save_model(request, obj, form, change)
    

