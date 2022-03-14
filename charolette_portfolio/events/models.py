from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Events(models.Model):
    background_image = ImageField(null=True, help_text='Background image for the events header.')
    header_title = models.CharField(default='Events', max_length=50, help_text='Title for the events header.')    
    
    title = models.CharField(null=True, max_length=50, help_text='Title for the event.')
    description = models.TextField(null=True, max_length=650, help_text='Description for the event.')
    image = ImageField(null=True, help_text='Main image for the event post.')
    date = models.DateField(null=True)

    def __str__(self):
        return 'Event: ' + self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'



class Images(models.Model):
    event = models.ForeignKey(Events, default=None, on_delete=models.CASCADE)
    image = ImageField(verbose_name='Image')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
