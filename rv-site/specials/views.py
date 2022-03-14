from django.shortcuts import render

from .models import Special
from .models import  PageTitle as pt_specials
from .models import Seo as seo_specials
from sections.models import Header, Footer
from blog.models import Blog

from contact.forms import ContactForm


def specials_feed(request):

    seo = seo_specials.objects.filter(main_page='specials').last()

    ctx = {
        'header': Header.objects.last(),
        'page_title': pt_specials.objects.last(),
        'footer': Footer.objects.last(),
        'contact_form': ContactForm(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    ctx['specials'] = list()
    for special in Special.objects.all():
        if special.title.lower() == 'rally':
            ctx['specials'].insert(0, special)
        else:
            ctx['specials'].append(special)
            
    return render(request, 'specials/single.html', context=ctx)
