from django.db import models

# Create your models here.
class Contact(models.Model):
    display = models.BooleanField(default=True, verbose_name='Display This Section', help_text='Check to display this section.')
    section_title = models.CharField(default='Get in touch', max_length=50, help_text='Title for this section.')
    address = models.CharField(null=True, max_length=50, help_text='Your address.')
    phone = models.CharField(null=True, max_length=50, help_text='Your phone number')
    email = models.CharField(null=True, max_length=50, help_text='Your email.')

    class Meta:
        verbose_name_plural = 'Contact'
