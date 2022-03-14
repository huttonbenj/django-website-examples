import os

from django.shortcuts import render
from .models import SectionTitleDescription, Image, Slideshow, Service, ContactUs, Header, AboutUs, TypedText, SectionTitle, SocialMedia
from django.core.mail import send_mail
from django.core.mail import EmailMessage

CATEGORY_CHOICES = (

    ('commercial', 'commercial'),
    ('residential', 'residential'),
    ('otherconstruction', 'other construction'),
    ('renovation',  'renovation/remodaling'),
    ('outdoorprojects', 'outdoor projects'),
    ('smallerprojects', 'smaller projects'),
)

def home(request):
    portfolio_main = SectionTitleDescription.objects.all()
    images = Image.objects.all()
    slideshow = Slideshow.objects.all()
    service = Service.objects.all()
    contact = ContactUs.objects.all()
    about = AboutUs.objects.all()
    typed_text = TypedText.objects.all()
    header = Header.objects.all()
    service_title = SectionTitle.objects.all()
    social = SocialMedia.objects.all()

    header = None if len(header) == 0 else header[0]
    about_us = None if len(about) == 0 else about[0]
    typed = None if len(typed_text) == 0 else typed_text[0]
    serv_title = None if len(service_title) == 0 else service_title[0]
    social_media = None if len(social) == 0 else social[0]
    
    # home portfolio description
    p = None if len(portfolio_main) == 0 else portfolio_main
    if p == None: portfolio_main = None
    if not p == None:
        portfolio_main = [s for s in portfolio_main][0]
    
    # arrange slots
    non_slots = [j for j in images if str(j.slot_number) == 'None']
    [non_slots.insert(int(j.slot_number)-1, j)
     for j in images if not str(j.slot_number) == 'None']
    ordered_images = {i+1: j for i, j in enumerate(non_slots)}

    # pf category menu 
    no_cat_dups = []
    category_menu = {(s.cat_link, s.category.capitalize()) for s in ordered_images.values(
    ) if not str(s.category) == ''}
    [no_cat_dups.append(s) for s in category_menu if not s[0] in no_cat_dups]
    
    # get all slides for slideshow if any exist
    all_slides = [s for s in slideshow]
    slides = None if all_slides == [] else all_slides
    if not slides == None: no_cat_dups.append((str(all_slides[0].category).lower(), str(all_slides[0].category).capitalize()))
    
    # get all services
    s = {i+1: j for i, j in enumerate(service)}
    services = None if s == {} else s
    
    # contact us
    c = None if len(contact) == 0 else contact
    if c == None: contact_us = None
    if not c == None:
        contact_us = [s for s in contact][0]

    try:
        email_request = request._post
        if email_request:
            to = str(request.__dict__['_post']['to'])
            name = str(request.__dict__['_post']['name'])
            email = str(request.__dict__['_post']['email'])
            phone_number = str(request.__dict__['_post']['phone_number'])
            message = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage:\n\n*** {request.__dict__['_post']['message']} *** \n"
            subject = f"Website Inquiry from {name}"

            valid_name = [s for s in name if s.isdigit()]
            spam = True if len(valid_name) > 0 else False
            if spam == False: send_mail(subject, message, email, [to])

    except Exception as e:
        pass


    return render(request, 'home_portfolio/home.html', {
        'images': images,
        'categories': no_cat_dups,
        'portfolio_main': portfolio_main,
        'ordered_images': ordered_images,
        'slideshow': slides,
        'typed_text': typed_text,
        'services': services,
        'service_title': serv_title,
        'header': header,
        'contact_us': contact_us,
        'about': about_us,
        'typed': typed,
        'social_media': social_media,
    })


