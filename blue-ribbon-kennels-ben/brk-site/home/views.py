from django.shortcuts import render

from main.models import Logo
from .models import Slide, Testimonial, TestimonialSection
from services.models import Service
from gallery.models import Image
from about.models import AboutTab, AboutAccordian, AboutPage
from faqs.models import AccordionEntry

# Create your views here.
def index(request):
    ctx = {
        'logo': Logo.objects.last(),
        'slides': Slide.objects.all(),
        'services': Service.objects.all().order_by('slot_position'),
        'gallery_images': Image.objects.all(),
        'testimonials_section_obj': TestimonialSection.objects.last(),
        'testimonials': Testimonial.objects.all(),
        'about_page_obj': AboutPage.objects.last(),
        'about_sections': AboutTab.objects.all().order_by('order_num'),
        'accordion_entries': AboutAccordian.objects.all().order_by('order_num'),
        'faqs': AccordionEntry.objects.all().order_by('order_num'),
        # 'parallax_img': Image.objects.first().image

    }

    if Image.objects.exists():
        ctx['parallax_img'] = Image.objects.first().image
    # only return max of eight gallery images for home page
    if len(ctx['gallery_images']) >= 8:
        ctx['gallery_images'] = ctx['gallery_images'][:9] 
        
    return render(request, 'home/index.html', context=ctx)
