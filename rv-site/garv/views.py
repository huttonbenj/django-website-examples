from django.shortcuts import render

from .models import Garv
from sections.models import Header, Footer
from blog.models import Blog

from contact.forms import ContactForm


def garv(request):

    ctx = {
        'garv_rules': Garv.objects.last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }

    return render(request, 'garv/garv.html', context=ctx)
