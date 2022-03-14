from django import forms
from django.forms import ModelForm
from .models import Contact, Email
from pyuploadcare.dj.forms import FileWidget, ImageField

class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}))
        self.fields['email'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Email'}))
        self.fields['phone'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Phone'}))
        self.fields['message'] = forms.CharField(required=True,
            widget=forms.Textarea(attrs={'class': 'custom-contact-form required form-control', 'placeholder': 'Type us a question here about your vacation rental or becoming an owner at Buena Vista!'}))

    class Meta:
        model = Contact
        fields = '__all__'


class EmailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['reservation_number'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Reservation Number'}))
        self.fields['email'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Email'}))
        self.fields['phone'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Phone'}))
        self.fields['coach_make'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coach Make'}))
        self.fields['coach_model'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coach Model'}))
        self.fields['coach_year'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coach Year'}))
        self.fields['coach_length'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coach Length'}))
        self.fields['trailer'] = forms.BooleanField(required=False,
            widget=forms.CheckboxInput(attrs={'class': 'form-control w-50px'}))
        self.fields['trailer_length'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Trailer Length'}))
        self.fields['pets'] = forms.BooleanField(required=False,
            widget=forms.CheckboxInput(attrs={'class': 'form-control w-50px', 'placeholder': ''}))
        self.fields['pet_breed'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pet Breed'}))
        self.fields['image'] = forms.ImageField(required=False)
    class Meta:
        model = Email
        fields = '__all__'
