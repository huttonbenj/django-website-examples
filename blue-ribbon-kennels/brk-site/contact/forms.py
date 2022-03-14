from django import forms
from django.forms import ModelForm
from .models import Contact

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
            widget=forms.Textarea(attrs={'class': 'custom-contact-form required form-control', 'placeholder': 'How can we help you?'}))

    class Meta:
        model = Contact
        fields = '__all__'