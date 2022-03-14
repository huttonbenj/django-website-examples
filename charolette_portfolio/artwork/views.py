from django.shortcuts import render
from .models import Artwork
from cart.models import Cart
from header.models import Header
from django.contrib import messages

# Create your views here.
def artwork(request):
    art = Artwork.objects.all()
    header = Header.objects.all()

    artwork = None if len(art) == 0 else [s for s in art]
    artwork_cats = None if len(art) == 0 else [s.image_category.upper() for s in artwork]
    artwork_sub_cats = None if len(art) == 0 else [s.image_sub_category.upper() for s in artwork if s.image_sub_category != None]
    if len(art) > 0: cats_subcats = artwork_cats + artwork_sub_cats
    framed_unframed = None if len(art) == 0 else [str(s.framed_unframed).lower() for s in artwork]

    header_navlogo = None if len(header) == 0 else [s for s in header][0]

    if len(art) > 0:

        return render(request, 'artwork/artwork.html', {
            'artwork': artwork,
            'artwork_cats': sorted(set(artwork_cats + artwork_sub_cats + framed_unframed)),
            'artwork_sub_cats': set(artwork_sub_cats),
            'cats_subcats': set(cats_subcats),
            'header_navlogo': header_navlogo,
        })
    else:
        return render(request, 'artwork/artwork.html')

def originals(request):
    art = Artwork.objects.all()
    header = Header.objects.all()

    artwork = None if len(art) == 0 else [s for s in art if str(s.image_category).lower() == 'originals']
    artwork_cats = None if len(art) == 0 else [str(s.image_category).upper() for s in artwork]
    artwork_sub_cats = None if len(art) == 0 else [str(s.image_sub_category).upper() for s in artwork if s.image_sub_category != None]
    framed_unframed = None if len(art) == 0 else [str(s.framed_unframed).lower() for s in artwork]
    cats_subcats = artwork_cats + artwork_sub_cats + framed_unframed

    header_navlogo = None if len(header) == 0 else [s for s in header][0]

    if len(art) > 0:
        return render(request, 'artwork/originals.html', {
            'artwork': artwork,
            'artwork_cats': set(artwork_cats),
            'artwork_sub_cats': sorted(set(artwork_sub_cats + framed_unframed)),
            'cats_subcats': set(cats_subcats),
            'header_navlogo': header_navlogo,
        })
    else:
        return render(request, 'artwork/artwork.html')

def oil(request):
    art = Artwork.objects.all()
    header = Header.objects.all()

    artwork = None if len(art) == 0 else [s for s in art if str(s.image_sub_category).lower() == 'oils']
    artwork_cats = None if len(art) == 0 else [str(s.framed_unframed).lower() for s in artwork]

    header_navlogo = None if len(header) == 0 else [s for s in header][0]
    if len(art) > 0:
        return render(request, 'artwork/oil.html', {
            'artwork': artwork,
            'artwork_cats': set(artwork_cats),
            'header_navlogo': header_navlogo,
        })
    else: 
        return render(request, 'artwork/artwork.html')


def watercolor(request):
    art = Artwork.objects.all()
    header = Header.objects.all()

    artwork = None if len(art) == 0 else [s for s in art if str(s.image_sub_category).lower() == 'watercolor']
    artwork_cats = None if len(art) == 0 else [str(s.framed_unframed).lower() for s in artwork]

    header_navlogo = None if len(header) == 0 else [s for s in header][0]
    
    if len(art) > 0:
        return render(request, 'artwork/watercolor.html', {
            'artwork': artwork,
            'artwork_cats': sorted(set(artwork_cats)),
            'header_navlogo': header_navlogo,
        })
    else:
        return render(request, 'artwork/artwork.html')

def prints(request):
    art = Artwork.objects.all()
    header = Header.objects.all()

    artwork = None if len(art) == 0 else [s for s in art if str(s.image_category).lower() == 'prints']
    artwork_cats = None if len(art) == 0 else [str(s.image_category).upper() for s in artwork]
    artwork_sub_cats = None if len(art) == 0 else [str(s.image_sub_category).upper() for s in artwork if s.image_sub_category != None]
    framed_unframed = None if len(art) == 0 else [str(s.framed_unframed).lower() for s in artwork]
    cats_subcats = artwork_cats + artwork_sub_cats + framed_unframed

    header_navlogo = None if len(header) == 0 else [s for s in header][0]

    if len(art) > 0:
        return render(request, 'artwork/prints.html', {
            'artwork': artwork,
            'artwork_cats': set(artwork_cats),
            'artwork_sub_cats': sorted(set(artwork_sub_cats + framed_unframed)),
            'cats_subcats': set(cats_subcats),
            'header_navlogo': header_navlogo,
        })
    else:
        return render(request, 'artwork/artwork.html')


def framed(request):
    art = Artwork.objects.all()
    header = Header.objects.all()

    artwork = None if len(art) == 0 else [s for s in art if str(s.framed_unframed).lower() == 'framed']
    artwork_cats = None if len(art) == 0 else [str(s.image_category).upper() for s in artwork]
    artwork_sub_cats = None if len(art) == 0 else [str(s.image_sub_category).upper() for s in artwork if str(s.image_sub_category) != 'None']
    header_navlogo = None if len(header) == 0 else [s for s in header][0]

    if len(art) > 0:
        return render(request, 'artwork/framed.html', {
            'artwork': artwork,
            'artwork_cats': sorted(set(artwork_cats + artwork_sub_cats)),
            'header_navlogo': header_navlogo,
        })
    else:
        return render(request, 'artwork/artwork.html')


def unframed(request):
    art = Artwork.objects.all()
    header = Header.objects.all()

    artwork = None if len(art) == 0 else [s for s in art if str(s.framed_unframed).lower() == 'unframed']
    artwork_cats = None if len(art) == 0 else [str(s.image_category).upper() for s in artwork]
    artwork_sub_cats = None if len(art) == 0 else [str(s.image_sub_category).upper() for s in artwork if str(s.image_sub_category) != 'None']
    header_navlogo = None if len(header) == 0 else [s for s in header][0]

    if len(art) > 0:
        return render(request, 'artwork/unframed.html', {
            'artwork': artwork,
            'artwork_cats': sorted(set(artwork_cats + artwork_sub_cats)),
            'header_navlogo': header_navlogo,
        })
    else:
        return render(request, 'artwork/artwork.html')



