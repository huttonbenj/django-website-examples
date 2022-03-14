from django.shortcuts import render
from main.models import Logo
from .models import FacilityPage, Image
# Create your views here.
def index(request):
    ctx = {
        'logo': Logo.objects.last(),
        'page_obj': FacilityPage.objects.last(),
        'images': Image.objects.all()
    }
    return render(request, 'facility/index.html', context=ctx)