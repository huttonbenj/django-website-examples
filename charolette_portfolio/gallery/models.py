from django.db import models
from pyuploadcare.dj.models import ImageField


# Create your models here.
class Gallery(models.Model):
    display = models.BooleanField(default=True, verbose_name='Display This Section', help_text='Check to display this section.')
    section_title = models.CharField(default='Gallery', max_length=50, help_text='Title for this section.')
    title = models.CharField(null=True, max_length=100, help_text='Image Title.')
    image = ImageField(null=True, help_text='Image to display for gallery')
    category = models.CharField(null=True, max_length=100, help_text='Image Category')
    style = models.CharField(default='staggred', choices=(('staggered', 'staggered'), ('even', 'even')), max_length=50, help_text='Gallery style.')

    class Meta:
        verbose_name_plural = 'Gallery'
