from django.db import models
from pyuploadcare.dj.models import ImageField

CATERGORY_CHOICES = (
    ('all artwork', 'all artwork'),
    ('originals', 'originals'),
    ('prints', 'prints'),
)

# Create your models here.
class Shop(models.Model):
    display = models.BooleanField(default=True, verbose_name='Display This Section', help_text='Check to show this section on the home page')
    title = models.CharField(null=True, max_length=100, help_text='Title for this post')
    description = models.CharField(null=True, max_length=100, help_text='Description of this shopping category')
    thumbnail = ImageField(null=True, verbose_name='thumbnail', help_text='Image to display')
    category = models.CharField(null=True, choices=CATERGORY_CHOICES, max_length=100, help_text='Category of Art')

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shop'
