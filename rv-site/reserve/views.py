from django.shortcuts import render
from sections.models import Header, Footer

from .models import Intro, Rule, WarningMessage
from .models import Seo as seo_reserve

from blog.models import Blog
from reserve.models import Seo as seo_reserve

from contact.forms import ContactForm

# Create your views here.
def reserve(request):

    seo = seo_reserve.objects.filter(main_page='reserve').last()

    ctx = {
        'intro': Intro.objects.last(),
        'rules': Rule.objects.all(),
        'warning': WarningMessage.objects.last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    return render(request, 'reserve/reserve.html', context=ctx)

