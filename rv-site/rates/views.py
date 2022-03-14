from django.shortcuts import render

from sections.models import Header, Footer
from .models import Package 
from .models import Seo as seo_rates
from .models import PageTitle as pt_rates

from blog.models import Blog

from contact.forms import ContactForm

# Create your views here.
def rates(request):

    seo = seo_rates.objects.filter(main_page='rates').last()

    ctx = {
        'packages': Package.objects.all().order_by('name'),
        'page_title': pt_rates.objects.last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    return render(request, 'rates/rates.html', context=ctx)
