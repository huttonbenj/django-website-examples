from pyuploadcare.dj.models import ImageField
from django.db import models

# Create your models here.


class About(models.Model):

    professional_photo = ImageField(null=True, verbose_name='Professional Photo', help_text='This is a photo for the about section')
    section_title = models.CharField(default='About Me', max_length=50, verbose_name='Section Title', help_text='Title for the about section.')
    description = models.TextField(null=True, help_text='This is the description for the about section.')
    background_image = ImageField(null=True, verbose_name='Background Image', help_text='This is the background image for the about section')

    class Meta:
        verbose_name_plural = 'About'