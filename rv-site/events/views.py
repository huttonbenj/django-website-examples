from django.shortcuts import render
from datetime import datetime

from sections.models import Header, Footer

from .models import Event
from .models import Seo as seo_events
from .models import PageTitle as pt_events

from blog.models import Blog

from contact.forms import ContactForm


# Create your views here.
def single(request, slug):

    event = Event.objects.get(seo__slug=slug)
    seo = seo_events.objects.filter(event=event).last()

    ctx = {
        'event': event,
        'events_timeline': Event.objects.filter(datetime__gte=datetime.now()).order_by('datetime'),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'page_title': pt_events.objects.filter(event=event).last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }
    return render(request, 'events/single.html', context=ctx)


def events(request):

    seo = seo_events.objects.filter(main_page='event_feed').last()

    ctx = {
        'events': Event.objects.filter(datetime__gte=datetime.now()).order_by('datetime'),
        'page_title': pt_events.objects.filter(event__isnull=True).last(),
        'header': Header.objects.last(),
        'footer': Footer.objects.last(),
        'seo': seo,
        'meta_tags': seo.meta_tags,
        'contact_form': ContactForm(),
        'blogs': Blog.objects.all().order_by('-datetime'),
    }
    
    return render(request, 'events/feed.html', context=ctx)
