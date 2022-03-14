from django.shortcuts import render
from main.models import Logo
from .models import FaqPage, AccordionEntry

# Create your views here.
def index(request):
    ctx = {
        'logo': Logo.objects.last(),
        'page_obj': FaqPage.objects.last(),
        'faqs': AccordionEntry.objects.all().order_by('order_num')
    }
    return render(request, 'faqs/index.html', context=ctx)