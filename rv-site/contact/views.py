from django.shortcuts import render, redirect
from .forms import ContactForm, EmailForm
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template import loader

from main.settings import MEDIA_ROOT


# Create your views here.
def contact_form_submit(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        body = f'''Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nPhone: {form.cleaned_data['phone']}\nMessage: {form.cleaned_data['message']}'''
        send_mail('Home Page Contact Form', body, form.cleaned_data['email'],
            ['info@buenavistaorangebeach.com'], fail_silently=False)
    return redirect(request.META.get('HTTP_REFERER'))


def contact_form_submit_footer(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        body = f'''Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nPhone: {form.cleaned_data['phone']}\nMessage: {form.cleaned_data['message']}'''
        send_mail('Footer Contact Form', body, form.cleaned_data['email'],
            ['info@buenavistaorangebeach.com'], fail_silently=False)
    return redirect(request.META.get('HTTP_REFERER'))


def contact_form_submit_lots(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        body = f'''Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nPhone: {form.cleaned_data['phone']}\nMessage: {form.cleaned_data['message']}'''
        send_mail('Lot Page Contact Form', body, form.cleaned_data['email'],
            ['info@buenavistaorangebeach.com'], fail_silently=False)
    return redirect(request.META.get('HTTP_REFERER'))

def email_form_submit(request):
    form = EmailForm
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email_context = {
                'reservation_number': form.cleaned_data['reservation_number'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'coach_make': form.cleaned_data['coach_make'],
                'coach_model': form.cleaned_data['coach_model'],
                'coach_year': form.cleaned_data['coach_year'],
                'coach_length': form.cleaned_data['coach_length'],
                'trailer': form.cleaned_data['trailer'],
                'trailer_length': form.cleaned_data['trailer_length'],
                'pets': form.cleaned_data['pets'],
                'pet_breed': form.cleaned_data['pet_breed'],
                }
            html_content = loader.get_template('%s.html' %  'contact/email_template').render(email_context)
            email_from = form.cleaned_data['email']
            email_to = ['info@buenavistaorangebeach.com']
            msg = EmailMultiAlternatives(
                                        subject='RV Specifications', 
                                        body=html_content, 
                                        from_email=email_from, 
                                        to=email_to,
                                        reply_to=[form.cleaned_data['email']]
                                        )
            if form.cleaned_data['image']:
                attachment = open(MEDIA_ROOT + f"/uploads/{form.cleaned_data['image'].name}", 'rb')
                msg.attach(form.cleaned_data['image'].name, attachment.read(), 'text/plain')
            msg.content_subtype = 'html'
            msg.send()

        return redirect('blogs')

    ctx = {}
    ctx['form'] = form

    return render(request, 'contact/email_form.html', context=ctx)
