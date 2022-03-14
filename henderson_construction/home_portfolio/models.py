import os
from django.db import models
from pyuploadcare.dj.models import ImageField
from dynamic_validator import ModelFieldRequiredMixin
from polymorphic.models import PolymorphicModel
from polymorphic.showfields import ShowFieldType

TRUE_FALSE = (
    ('True', 'True'),
    ('False', 'False')
)

PF_CATEGORIES = (
    ('None', 'None'),
    ('commercial', 'commercial'),
    ('residential', 'residential'),
    ('otherconstruction', 'other construction'),
    ('renovation', 'renovation'),
    ('outdoorprojects', 'outdoor projects'),
    ('smallerprojects', 'smaller projects'),
)

PF_SLOTS = (
    ('None', 'None'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)

BG_LOCATION = (
    ('header', 'header'),
    ('typed text', 'typed text')

)

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class Portfolio(PolymorphicModel):
    class Meta:
        verbose_name_plural = 'Portfolio'

class Image(Portfolio):
    photo = ImageField(null=True, verbose_name='image')
    category = models.CharField(
        default='', max_length=50)
    cat_link = models.CharField(default='', max_length=50)
    slot_number = models.CharField(
        default='None', max_length=50, choices=PF_SLOTS, blank=True)
    description = models.CharField(
        default='', max_length=200, blank=True)

class SectionTitleDescription(Portfolio):
    title = models.CharField(default='', max_length=50)
    description = models.TextField(
        default='', max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Portfolio Title & Description"

class Slideshow(Portfolio):
    slide_photo = ImageField(null=True, verbose_name='image')
    category = models.CharField(
        default='', max_length=50)

    class Meta:
        verbose_name_plural = "Portfolio Slideshow"

class SocialMedia(models.Model):
    facebook_link = models.CharField(
            default='', max_length=150, blank=True)
    instagram_link = models.CharField(
        default='', max_length=150, blank=True)

    class Meta:
        verbose_name_plural = "Social Media"

class Header(models.Model):
    logo = ImageField(null=True)
    description = models.TextField(default='', max_length=200, blank=True)
    on_break = models.CharField(default='', max_length=50, blank=True)
    background = ImageField(null=True)
    video_modal = models.BooleanField(default=False)
    youtube_url = models.CharField(default='', max_length=150, blank=True)

    class Meta:
        verbose_name_plural = "Header"

class AboutUs(models.Model):
    title = models.CharField(default='', max_length=50)
    image = ImageField(null=True)
    left_text = models.TextField(default='', max_length=200, blank=True)
    on_break = models.CharField(null=True, max_length=50, blank=True)
    right_title = models.CharField(default='', max_length=50, blank=True)
    right_text = models.TextField(default='', max_length=200, blank=True)
    number_of_progress_bars = models.IntegerField(default=0, blank=True)
    progress_bar_title_1 = models.CharField(
        null=True, max_length=20, blank=True)
    progress_bar_title_2 = models.CharField(
        null=True, max_length=20, blank=True)
    progress_bar_title_3 = models.CharField(
        null=True, max_length=20, blank=True)
    progress_bar_title_4 = models.CharField(
        null=True, max_length=20, blank=True)
    name_and_signature = models.BooleanField(default=True, blank=True)
    signature_file = models.FileField(default='', blank=True, upload_to='signature/')

    class Meta:
        verbose_name_plural = "About Us"

class TypedText(models.Model):
    background = ImageField(null=True)
    static_text = models.CharField(default='', max_length=50, blank=True)
    typed_text_1 = models.CharField(default='', max_length=50, blank=True)
    typed_text_2 = models.CharField(default='', max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Background (Typed Text)"

class Services(PolymorphicModel):
    class Meta:
        verbose_name_plural = "Services"

class SectionTitle(Services):
    title = models.CharField(default='', max_length=50)
    
    class Meta:
        verbose_name_plural = "Services Main Title"

class Service(Services):
    title = models.CharField(default='', max_length=50)
    description = models.TextField(
        default='', max_length=200, blank=True)
    icon = models.FileField(default='None', upload_to='icons/')

class ContactUs(models.Model):
    title = models.CharField(default='', max_length=50)
    description = models.TextField(
        default='', max_length=200, blank=True)
    address = models.CharField(default='', max_length=150, blank=True)
    email = models.CharField(default='', max_length=150, blank=True)
    phone_number = models.CharField(default='', max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Contact Us"
