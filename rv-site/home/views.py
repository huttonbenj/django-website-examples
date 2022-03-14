from django.shortcuts import render
from sections.models import Header, Slide, Intro, Overview, PackageItem, About, Testimonial, Testimonials, Footer

from blog.models import Blog
from lots.models import Lot
from ownership.models import LotForSale
from contact.forms import ContactForm
from itertools import chain


def home(request):
    ctx = {
        'home': True,
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'slider': Slide.objects.all().order_by('order_slot'),
        'intro': Intro.objects.last(),
        'overview': Overview.objects.all().order_by('position_slot'),
        'testimonials': Testimonial.objects.all(),
        'packages': PackageItem.objects.all().order_by('package__name'),
        'about': About.objects.all().order_by('position_slot'),
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
        'lots': Lot.objects.all(),
        'empty_lots_for_sale' : [lot.lot.id for lot in LotForSale.objects.filter(empty_lot=True)],
        'pending_sale' : [lot.lot.id for lot in LotForSale.objects.filter(pending_sale=True)],
    }

    if len(Testimonials.objects.all()) > 0:
        ctx['testimonial_bg_image'] = Testimonials.objects.first().background_image.url

    return render(request, 'home/landing.html', context=ctx) 
