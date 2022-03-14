from django.shortcuts import render, redirect
from header.models import Header
from shop.models import Shop
from contact.models import Contact
from artwork.models import Artwork
from about.models import About
from contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from charolette_portfolio.settings import SENDGRID_API_KEY
from django.contrib import messages

import datetime

# Create your views here.
def home(request, *args, **kwargs):
        remove = request.GET.get('remove')
        if remove != None and 'http' in remove:
            return redirect(f'cart/?remove_item=True')

        # Get all objects
        header_objs = Header.objects.all()
        shop_objs = Shop.objects.all()
        about_objs = About.objects.all()

        contact_objs = Contact.objects.all()
        artwork_objs = Artwork.objects.all()

        # Header
        header = None if len(header_objs) == 0 else header_objs[len(header_objs)-1]

        # Shop
        shop = None if len(shop_objs) == 0 else [s for s in shop_objs]

        #About
        about = None if len(about_objs) == 0 else [s for s in about_objs]

        # Artwork
        artwork = None if len(artwork_objs) == 0 else [s for s in artwork_objs]
        artwork_cats = None if len(artwork_objs) == 0  else [str(s.image_category).upper() for s in artwork_objs]
        artwork_sub_cats = None if len(artwork_objs) == 0 else [str(s.image_sub_category).upper() for s in artwork if s.image_sub_category != None]
        if len(artwork_objs) > 0: cats_subcats = artwork_cats + artwork_sub_cats
        framed_unframed = None if len(artwork_objs) == 0 else [str(s.framed_unframed).lower() for s in artwork]

        # Home Gallery
        gallery_four = None if len(artwork_objs) == 0 else [s for s in artwork_objs][:4]
        gallery_eight = None if len(artwork_objs) == 0 else [s for s in artwork_objs][:8]
        gallery_twelve = None if len(artwork_objs) == 0 else [s for s in artwork_objs][:12]

        gallery_cats_four = None if len(artwork_objs) == 0 else [s.image_category.upper() for s in gallery_four]
        gallery_cats_eight = None if len(artwork_objs) == 0 else [s.image_category.upper() for s in gallery_eight]
        gallery_cats_twelve = None if len(artwork_objs) == 0 else [s.image_category.upper() for s in gallery_twelve]

        num_of_photos = None if len(artwork_objs) == 0 else [s.number_of_photos for s in artwork_objs]
        if not num_of_photos == None: num_of_photos = num_of_photos[0]

        if num_of_photos == '4':
            gallery = gallery_four
            gallery_cats = gallery_cats_four
        elif num_of_photos == '8':
            gallery = gallery_eight
            gallery_cats = gallery_cats_eight
        elif num_of_photos == '12':
            gallery = gallery_twelve
            gallery_cats = gallery_cats_twelve
        else:
            gallery = None
            gallery_cats = None



        print(gallery)
        # Contact
        contact = None if len(contact_objs) == 0 else [s for s in contact_objs][0]
        if request.method == 'GET':
                form = ContactForm()
        else:
                form = ContactForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            message = Mail(
                from_email=from_email,
                to_emails='charlottemeadows@gmail.com',
                subject=subject,
                html_content=message)
            try:
                sg = SendGridAPIClient(SENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                messages.add_message(request, messages.INFO, 'Your email was successfully sent!  I will get back to you as soon as possible!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

        if len(artwork_objs) > 0:
                return render(request, 'home/home.html', {
                        'header': header,
                        'shop': shop,
                        'artwork': artwork,
                        'artwork_cats': sorted(set(artwork_cats + artwork_sub_cats + framed_unframed)),
                        'gallery': gallery,
                        'contact': contact,
                        'about':about,
                        'form':form
                        })

        else:
                return render(request, 'home/home1.html')


def successView(request):
    return render(request, 'contact/success.html')
