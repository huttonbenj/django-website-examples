from django.shortcuts import render
from sections.models import Header, Footer

from .models import LotForSale, OwnerForms
from .models import Seo as seo_ownership
from .models import PageTitle as pt_ownership

from blog.models import Blog
from ownership.models import Seo as seo_ownership

from contact.forms import ContactForm


# Create your views here.
def ownership(request):

    seo = seo_ownership.objects.filter(main_page='ownership_feed').last()

    ctx = {
        'lots': LotForSale.objects.all().order_by('lot__number'),
        # 'pending': [obj.lot.id for obj in LotForSale.objects.filter(pending_sale=True)],
        'header': Header.objects.last(),
        'page_title': pt_ownership.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    return render(request, 'ownership/ownership.html', context=ctx)

def owner_forms(request):

    seo = seo_ownership.objects.filter(main_page='ownership_feed').last()

    ctx = {
        'lots': LotForSale.objects.all().order_by('lot__number'),
        'header': Header.objects.last(),
        'page_title': pt_ownership.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'owner_forms': OwnerForms.objects.all(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

  
    return render(request, 'ownership/owner_forms.html', context=ctx)
