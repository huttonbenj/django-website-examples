from django.shortcuts import render
from .models import Lot
from .models import Seo as seo_lots
from .models import PageTitle as pt_lots

from sections.models import Header, Footer
from blog.models import Blog
from lots.models import Seo as seo_lots
from ownership.models import LotForSale
from contact.forms import ContactForm 


# Create your views here.
def single(request, id):

    seo = seo_lots.objects.filter(main_page='lots').last()

    ctx = {
        'lot': Lot.objects.get(id=id),
        'page_title': pt_lots.objects.last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo_lots.objects.filter(main_page='lots').last(),
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }


    if 'ownership' in request.META['HTTP_REFERER']:
        lot_for_sale = LotForSale.objects.filter(lot=ctx['lot'])
        if lot_for_sale:
            ctx['lot_price'] = '{:,}'.format(lot_for_sale.first().price)
    
    return render(request, 'lots/lot-single.html', context=ctx)


def lot_map(request):

    seo = seo_lots.objects.filter(main_page='lots').last()

    ctx = {
        'lots': Lot.objects.all(),
        'empty_lots_for_sale' : [lot.lot.id for lot in LotForSale.objects.filter(empty_lot=True)],
        'pending' : [lot.lot.id for lot in LotForSale.objects.filter(pending_sale=True)],
        'page_title': pt_lots.objects.last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo_lots.objects.filter(main_page='lots').last(),
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    return render(request, 'lots/site-map.html', context=ctx)
