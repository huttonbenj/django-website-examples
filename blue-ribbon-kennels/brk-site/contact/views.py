from django import forms
from django.shortcuts import render
from main.models import Logo
from django.http import JsonResponse, response
from .forms import ContactForm

# Create your views here.
def index(request):
    ctx = {
        'logo': Logo.objects.last(),
    }
    return render(request, 'contact/index.html', context=ctx)


def ajax_submit(request):

    form = ContactForm(request.POST)
    data = {}
    if form.is_valid():
        form.save()
    else:
        data['errors'] = form.errors
       
    return JsonResponse(data)