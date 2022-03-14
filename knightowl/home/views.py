from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, PricingForm

def home(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            try:
                name = contact_form.cleaned_data['name']
                subject = contact_form.cleaned_data['subject']
                from_email = contact_form.cleaned_data['from_email']
                message = contact_form.cleaned_data['message']
                body = 'Name: {0}\n Email: {1}\n Message: {2}'.format(name, from_email, message)
                send_mail(subject, body, from_email, ['knightowlstudios.web@gmail.com'])
                return render(request, 'home/success_contact.html')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, "home/home.html", {'contact_form': contact_form})


def pricing_request(request):
    if request.method == 'GET':
        price_quote = PricingForm()

    if request.method == 'POST':
        price_quote = PricingForm(request.POST)
        if request.POST.get("back"):
            return redirect('home')

        if request.POST.get("submit") and price_quote.is_valid():
            try:
                first_name = price_quote.cleaned_data['first_name']
                last_name = price_quote.cleaned_data['last_name']
                from_email = price_quote.cleaned_data['from_email']
                phone = price_quote.cleaned_data['phone']
                business_name = price_quote.cleaned_data['business_name']
                business_category = price_quote.cleaned_data['business_category']
                desired_website_name = price_quote.cleaned_data['desired_website_name']
                num_pages = price_quote.cleaned_data['num_pages']
                google_analytics = price_quote.cleaned_data['google_analytics']
                google_maps = price_quote.cleaned_data['google_maps']
                user_accounts = price_quote.cleaned_data['user_accounts']
                payment_portal = price_quote.cleaned_data['payment_portal']
                message = price_quote.cleaned_data['message']
                body = 'First Name: {0}\n Last Name: {1}\n Email: {2}\n Phone: {3}\n Business Name: {4}\n Business Category: {5}\n Desired Website Name: {6}\n Number of Web Pages: {7}\n  Google Analytics: {8}\n Google Maps: {9}\n User Accounts: {10}\n Payment Portal: {11}\n Message: {12}'.format(first_name, last_name, from_email, phone, business_name, business_category, desired_website_name, num_pages, google_analytics, google_maps, user_accounts, payment_portal, message)
                send_mail('Website Price Quote Inquiry', body, from_email, ['knightowlstudios.web@gmail.com'])
                return render(request, "home/success_pricequote.html")

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, 'home/pricing_request.html')