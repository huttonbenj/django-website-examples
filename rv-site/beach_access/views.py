from django.shortcuts import render
from sections.models import Header, Footer
from blog.models import Blog

from contact.forms import ContactForm

def beach_access(request):
    ctx = {
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }
    return render(request, 'beach_access/beach_access.html', context=ctx)
