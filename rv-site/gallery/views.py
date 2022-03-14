from django.shortcuts import render

from .models import Gallery
from .models import Seo as seo_gallery
from .models import PageTitle as pt_gallery

from sections.models import Header, Footer
from blog.models import Blog

from contact.forms import ContactForm

# Create your views here.
def gallery(request):

    seo = seo_gallery.objects.filter(main_page='gallery').last()

    ctx = {
        'gallery': Gallery.get_objs(),
        'categories': [s for s in Gallery.get_categories()],
        'header': Header.objects.last(),
        'page_title': pt_gallery.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    return render(request, 'gallery/main.html', context=ctx)
