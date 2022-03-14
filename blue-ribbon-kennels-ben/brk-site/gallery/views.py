from django.http import request
from django.shortcuts import render
from .models import GalleryPage, Image
from main.models import Logo

# Create your views here.
def gallery(request):
    ctx = {
        'logo': Logo.objects.last(),
        'page_obj': GalleryPage.objects.last(),
        'gallery_images': Image.objects.all(),
        'categories': Image.get_category_filters()
    }
    return render(request, 'gallery/index.html', context=ctx)