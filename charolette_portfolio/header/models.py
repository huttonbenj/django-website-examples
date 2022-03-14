from django.db import models
from pyuploadcare.dj.models import ImageField
from django.core.exceptions import ValidationError

GALLERY_STYLE_CHOICES = (
    ('simple', 'simple'),
    ('textbox', 'textbox'),
    ('animated', 'animated'),
    ('logo', 'logo')
)


# Create your models here.
class Header(models.Model):
    display = models.BooleanField(default=True, verbose_name='Display This Section', help_text='Check to display this section.')
    bg = ImageField(null=True, verbose_name='Background', help_text='Background Image.')
    intro = models.CharField(null=True, max_length=100, help_text='A short intro.')
    name = models.CharField(null=True, max_length=100, help_text='Your Name.')
    navlogo = ImageField(null=True, verbose_name='Nav Logo', help_text='Logo that appears in the top left corner of the Navigation Bar.')
    logo = ImageField(null=True, verbose_name='logo', help_text='The logo that will be used if you use the "Logo Styled Header Option".')
    style = models.CharField(choices=GALLERY_STYLE_CHOICES, default='animated', max_length=50, verbose_name='Style', help_text='The style header you want to use.')

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'
