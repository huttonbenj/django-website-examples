from django import forms
from django.forms import ModelForm
from .models import Kennel, Reservation
from django.contrib.admin import widgets                                       

# class ReservationForm(forms.ModelForm):
#     def clean(self):
#         self.instance.kennel = Kennel.get_availabile()
#         cleaned_data = super().clean()
#         return cleaned_data


#     def save(self, commit=True):
#         res = super(ReservationForm, self).save(commit=False)
#         res.set_kennel(self.fields.kennel)
#         if commit:
#             res.save()
#         return res

#     class Meta:
#         model = Reservation
#         fields = '__all__'


class ReservationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Reservation Number'}))
        self.fields['start_date'] = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control text-start', 'disabled':True, 'placeholder':'Select a date'}))
        self.fields['end_date'] = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control text-start', 'disabled':True, 'placeholder':'Select a date'}))
        self.fields['start_date_additional'] = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control text-start', 'disabled':True, 'placeholder':'Select a date'}))
        self.fields['end_date_additional'] = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control text-start', 'disabled':True, 'placeholder':'Select a date'}))
        # self.fields['extended_stay'] = forms.BooleanField(required=False,
        #     widget=forms.CheckboxInput(attrs={'class': 'form-control w-50px', 'placeholder': ''}))
        self.fields['pickup_date'] = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control text-start', 'disabled':True, 'placeholder':'Select a date'}))
        # self.fields['number_of_days'] = forms.CharField(required=True,
        #     widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Coach Length'}))
        # self.fields['cost'] = forms.IntegerField(required=False,
        #     widget=forms.NumberInput(attrs={'class': 'form-control w-50px'}))
        # self.fields['additional_cost'] = forms.CharField(required=False,
        #     widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Trailer Length'}))
        # self.fields['overall_cost'] = forms.CharField(required=False,
        #     widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Pet Breed'}))
        # self.fields['full_range_end_date'] = forms.CharField(required=False,
        #     widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Pet Breed'}))
        self.fields['first_name'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Your First Name'}))
        self.fields['last_name'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Your Last Name'}))
        self.fields['email'] = forms.EmailField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Your Email'}))
        self.fields['phone'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Your Phone Number'}))
        self.fields['street'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Your Street'}))
        self.fields['city'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Your City'}))
        self.fields['state'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Your State'}))
        self.fields['postal_code'] = forms.IntegerField(required=False,
            widget=forms.NumberInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Postal Code'}))
        self.fields['dogs_name'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': "Dog's Name"}))
        self.fields['dogs_breed'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': "Dog's Breed"}))
        self.fields['dogs_sex'] = forms.ChoiceField(required=False,
            widget=forms.Select(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': "Dog's Sex"}), choices=( (('-------------', '-------------'), ('male', 'Male'), ('female', 'Female')) ))
        self.fields['dogs_age'] = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': "Dog's Age"}))
        self.fields['comments'] = forms.CharField(required=False,
            widget=forms.Textarea(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Enter Any Additional Comments (optional)'}))
        # self.fields['status'] = forms.CharField(required=False,
        #     widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Pet Breed'}))
        # self.fields['session_key'] = forms.CharField(required=False,
        #     widget=forms.TextInput(attrs={'class': 'sm-form-control border-form-control required', 'placeholder': 'Pet Breed'}))
        self.fields['shot_records'] = forms.FileField(required=False,  widget=forms.FileInput(attrs={'class':'sm-form-control border-form-control'}))
    class Meta:
        model = Reservation
        fields = '__all__'


    #  = models.CharField(max_length=100, null=True, blank=False, choices=RESERVATION_TYPES)
    # # start_date = models.DateField(null=True, blank=False, validators=[current_future_date])
    # # end_date = models.DateField(null=True, blank=False, validators=[current_future_date])
    #  = models.DateField(null=True, blank=False)
    #  = models.DateField(null=True, blank=False)
    #  = models.DateField(null=True, blank=True)
    #  = models.DateField(null=True, blank=True)
    #  = models.BooleanField(default=False, verbose_name='Additional Days')
    #  = models.DateField(null=True, blank=True)
    #  = models.IntegerField(null=True, blank=True)
    #  = models.IntegerField(null=True, blank=True, verbose_name='Total Cost')
    #  = models.IntegerField(null=True, blank=True)
    #  = models.IntegerField(null=True, blank=True, verbose_name='Total Cost')
    #  = models.DateField(null=True, blank=True)
    #  = models.CharField(max_length=100, null=True, blank=False)
    #  = models.CharField(max_length=100, null=True, blank=False)
    #  = models.EmailField(null=True, blank=False)
    #  = models.CharField(null=True, blank=False, max_length=25)
    #  = models.CharField(null=True, blank=False, max_length=255)
    #  = models.CharField(null=True, blank=False, max_length=255)
    #  = models.CharField(null=True, blank=False, max_length=255)
    #  = models.IntegerField(null=True, blank=False)
    #  = models.CharField(max_length=100, null=True, blank=False)
    #  = models.CharField(max_length=100, null=True, blank=False)
    #  = models.CharField(max_length=25, null=True, blank=False, choices=(('male', 'Male'), ('female', 'Female')))
    #  = models.IntegerField(null=True, blank=False)
    #  = models.TextField(null=True, blank=True)
    #  = models.CharField(max_length=25, choices=(('closed','Closed'), ('active','Active'), ('upcoming','Upcoming')), null=True, blank=True)
    # # repeating = models.BooleanField(default=False)
    # # transfer_kennel = models.CharField(max_length=25, choices=((str(num), str(num)) for num in range(1,57)), null=True, blank=True)
    #  = models.CharField(null=True, blank=False, max_length=255)
    #  = models.FileField(null=True, blank=True, upload_to='media/')