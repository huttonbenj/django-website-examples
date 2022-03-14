from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class PricingForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    business_name = forms.CharField(required=False)
    business_category = forms.CharField(required=False)
    desired_website_name = forms.CharField(required=False)
    num_pages = forms.IntegerField(required=False)
    google_analytics = forms.BooleanField(required=False)
    google_maps = forms.BooleanField(required=False)
    user_accounts = forms.BooleanField(required=False)
    payment_portal = forms.BooleanField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)

    



