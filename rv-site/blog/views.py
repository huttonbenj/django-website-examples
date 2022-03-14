from django.shortcuts import render
from datetime import datetime

from sections.models import Header, Footer

from .models import Blog
from .models import Seo as seo_blog
from .models import PageTitle as pt_blog

from contact.forms import ContactForm

# Create your views here.
def single(request, slug):

    blog = Blog.objects.get(seo__slug=slug)
    seo = seo_blog.objects.filter(blog=blog).last()

    ctx = {
        'blog': blog,
        'page_title': pt_blog.objects.filter(blog=blog).last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    return render(request, f'blog/single-image.html', context=ctx)


def blogs(request):
    seo = seo_blog.objects.filter(main_page='blog_feed').last()

    ctx = {
        'page_title': pt_blog.objects.filter(blog__isnull=True).last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'contact_form': ContactForm(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'blogs': Blog.objects.filter(datetime__lte=datetime.now()).order_by('-datetime'),
    }

    if 'caldera_forms_preview' in str(request.META.get('HTTP_REFERER')):
        ctx['success_message'] = True 
        ctx['message'] = 'Your form was successfully submitted, check out our blog feed!'

    return render(request, 'blog/feed.html', context=ctx)
