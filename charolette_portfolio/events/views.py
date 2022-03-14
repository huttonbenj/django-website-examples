from django.shortcuts import render
from .models import Events, Images
from header.models import Header

# Create your views here.
def events(request):
    events = Events.objects.all()

    header = Header.objects.all()
    header = None if len(header) == 0 else header[len(header)-1]

    return render(request, 'events/events.html', {
        'header': header, 
        'events': events
    })


def single_event(request):
    
    id = request.GET.get('id')
    event = Events.objects.get(id=id)

    try:
        images = Images.objects.filter(event_id=id)
    except Exception as e:
        images = None


    header = Header.objects.all()
    header = None if len(header) == 0 else header[len(header)-1]

    return render(request, 'events/single_event.html', {
        'header': header,
        'event': event,
        'images': images,
        'no_images': len(images)


    })

